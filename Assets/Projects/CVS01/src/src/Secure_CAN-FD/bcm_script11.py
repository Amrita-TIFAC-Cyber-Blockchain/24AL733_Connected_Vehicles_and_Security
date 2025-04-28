import os
import hashlib
import hmac
from Crypto.Cipher import AES

# Keys for AES and HMAC
AES_KEY = b"1234567890ABCDEF"
HMAC_KEY = b"THIS_IS_A_32_BYTE_KEY_FOR_HMAC_SHA256!"

#INPUT_FILE = "C:/Users/CB.EN.P2AEL24003/Desktop/Mait/CVS/New_ProjectWork/Secured_CAN-FD/received_data.bin"
#OUTPUT_FILE = "C:/Users/CB.EN.P2AEL24003/Desktop/Mait/CVS/New_ProjectWork/Secured_CAN-FD/bcm_output.txt"

INPUT_FILE = "C:/Users/CB.EN.P2AEL24003/Desktop/Mait/CVS/New_ProjectWork/Secured_CAN-FD/encrypted_data.bin"
OUTPUT_FILE = "C:/Users/CB.EN.P2AEL24003/Desktop/Mait/CVS/New_ProjectWork/Secured_CAN-FD/bcm_output.txt"

def decrypt_signal(encrypted_payload):
    """Decrypt the MsgID + Signal and validate HMAC."""
    encrypted_data = encrypted_payload[:16]  # First 16 bytes = Encrypted Data
    received_hmac = encrypted_payload[16:]  # Last 8 bytes = Received HMAC

    # Verify HMAC
    computed_hmac = hmac.new(HMAC_KEY, encrypted_data, hashlib.sha256).digest()[-8:]
    if computed_hmac != received_hmac:
        print("❌ HMAC Verification Failed!")
        return None, None

    # Decrypt using AES
    cipher = AES.new(AES_KEY, AES.MODE_ECB)
    decrypted_padded = cipher.decrypt(encrypted_data)

    # Extract MsgID and Signal Value
    msg_id = int.from_bytes(decrypted_padded[:2], 'big')
    signal_value = decrypted_padded[2]

    return msg_id, signal_value

def main():
    print("BCM Python Script Started!")

    if not os.path.exists(INPUT_FILE):
        print("❌ ERROR: received_data.bin NOT FOUND!")
        return

    with open(INPUT_FILE, "r") as f:
        encrypted_payload = list(map(int, f.read().strip().split()))

    encrypted_payload = bytes(encrypted_payload)

    msg_id, signal_value = decrypt_signal(encrypted_payload)

    if msg_id is None:
        print("❌ BCM ERROR: Message verification failed!")
        return

    if msg_id != 0x300:
        print("❌ BCM ERROR: Invalid MsgID received!")
        return

    print(f"✅ BCM SUCCESS: MsgID = {hex(msg_id)}, Signal Value = {signal_value}")

    # Write decrypted data to file
    with open(OUTPUT_FILE, "w") as f:
        f.write(f"{msg_id} {signal_value}")

if __name__ == "__main__":
    main()

input("Press Enter to continue...")
exit(0)
    