import sys
import os
import hashlib
import hmac
from Crypto.Cipher import AES

# Keys for AES and HMAC
AES_KEY = b"1234567890ABCDEF"  # 16-byte key
HMAC_KEY = b"THIS_IS_A_32_BYTE_KEY_FOR_HMAC_SHA256!"  # 32-byte key

def pad_data(data, block_size=16):
    """Pads the data to match AES block size."""
    padding_len = block_size - len(data) % block_size
    return data + bytes([padding_len] * padding_len)

def encrypt_signal(msg_id, signal_value):
    """Encrypt the MsgID + Signal using AES-ECB and compute HMAC-SHA256."""
    # Convert MsgID (0x300) to 2 bytes, Signal Value to 1 byte → Total 3 bytes
    raw_data = msg_id.to_bytes(2, 'big') + bytes([signal_value])
    
    # Pad to 16 bytes for AES encryption
    padded_data = pad_data(raw_data)
    
    cipher = AES.new(AES_KEY, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(padded_data)  # 16-byte output
    
    # Compute HMAC over the encrypted data
    hmac_digest = hmac.new(HMAC_KEY, encrypted_data, hashlib.sha256).digest()  # 32-byte output
    
    # Extract required bytes
    final_encrypted = encrypted_data[:16]  # First 16 bytes of AES output
    final_hmac = hmac_digest[-8:]  # Last 8 bytes of HMAC output
    
    return final_encrypted + final_hmac  # 24-byte result

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ('0', '1'):
        print("Usage: python script.py <0 or 1>")
        sys.exit(1)
    
    msg_id = 0x300  # Message ID to be encrypted
    signal_value = int(sys.argv[1])  # Convert command-line argument to integer
    encrypted_payload = encrypt_signal(msg_id, signal_value)
    
    # ✅ Write encrypted data to file
    with open("C:/Users/CB.EN.P2AEL24003/Desktop/Mait/CVS/New_ProjectWork/Secured_CAN-FD/encrypted_data.bin", "w") as f:
        f.write(" ".join(str(byte) for byte in encrypted_payload))  # Write numbers as space-separated values
    
    print("✅ Encrypted MsgID + Signal Value written to file!")

if __name__ == "__main__":
    main()

#input("Press Enter to continue...")
#exit(0)
    
