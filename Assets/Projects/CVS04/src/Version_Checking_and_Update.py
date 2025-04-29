import requests
import os
import subprocess

# Config
YOLO_REPO_API = "https://api.github.com/repos/ultralytics/ultralytics/releases/latest"
CURRENT_MODEL_PATH = "./models/yolov8n.pt"
MODEL_SAVE_DIR = "./models/"
MODEL_NAME = "yolov8n.pt"

def get_latest_release():
    response = requests.get(YOLO_REPO_API)
    if response.status_code == 200:
        release_info = response.json()
        return release_info["tag_name"], release_info["assets"]
    else:
        print("Failed to fetch release info")
        return None, None

def download_model(download_url, save_path):
    print(f"Downloading updated model from {download_url}")
    model_data = requests.get(download_url)
    with open(save_path, 'wb') as f:
        f.write(model_data.content)
    print(f"Model saved to {save_path}")

def trigger_mender_deployment():
    print("Triggering Mender client deployment...")
    subprocess.run(["mender", "-install", "artifact.mender"])
    subprocess.run(["mender", "-commit"])

def main():
    latest_version, assets = get_latest_release()
    if not latest_version or not assets:
        return

    # Here you can add logic if you want to skip minor version updates
    print(f"Latest YOLO Version: {latest_version}")

    # For simplicity, assume if asset has a new yolov8n.pt, it's newer
    for asset in assets:
        if MODEL_NAME in asset['name']:
            latest_model_url = asset['browser_download_url']
            latest_model_path = os.path.join(MODEL_SAVE_DIR, MODEL_NAME)

            # (Optional) Compare file checksum if you want to be smarter

            download_model(latest_model_url, latest_model_path)

            # Once updated, trigger OTA deployment
            trigger_mender_deployment()
            break
    else:
        print("No updated model found in latest release.")

if __name__ == "__main__":
    main()
