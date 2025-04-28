import os
import requests
import json
from dotenv import load_dotenv

# Load GitHub Token from .env file
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "Manishankarmolleti"
REPO_NAME = "ota-firmware"
DOWNLOAD_PATH = "firmware/"

# Ensure the download directory exists
os.makedirs(DOWNLOAD_PATH, exist_ok=True)

def get_latest_release():
    """Fetch the latest firmware release from GitHub."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases/latest"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch release: {response.status_code}, {response.text}")
        return None

def download_firmware(asset_url, asset_name):
    """Download firmware file from GitHub release."""
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(asset_url, headers=headers, stream=True)
    
    if response.status_code == 200:
        file_path = os.path.join(DOWNLOAD_PATH, asset_name)
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"✅ Firmware downloaded: {file_path}")
    else:
        print(f"❌ Download failed: {response.status_code}, {response.text}")

if __name__ == "__main__":
    release_data = get_latest_release()
    if release_data and "assets" in release_data:
        for asset in release_data["assets"]:
            if asset["name"].endswith(".bin") or asset["name"].endswith(".hex"):
                print(f"📥 Downloading {asset['name']}...")
                download_firmware(asset["browser_download_url"], asset["name"])
    else:
        print("⚠️ No firmware releases found!")
