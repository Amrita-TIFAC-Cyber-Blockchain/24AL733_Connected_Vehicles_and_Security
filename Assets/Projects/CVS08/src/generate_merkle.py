"""
generate_merkle.py

Scans a firmware directory for .bin files, builds a Merkle tree over their SHA-256 hashes,
signs the root hash with ECDSA-P256, and writes out:
 - metadata.json (with leaves, proof paths, root signature)
 - ecdsa_pub.pem (public key for verification)
"""
import os
import json
import argparse
import hashlib
from ecdsa import SigningKey, NIST256p

def sha256(data: bytes) -> bytes:
    """Compute SHA-256 digest."""
    return hashlib.sha256(data).digest()

def build_merkle(leaves: list[bytes]) -> list[list[bytes]]:
    """
    Build the Merkle tree layers.
    Returns a list of layers: layer[0] = leaves, layer[-1] = [root].
    """
    tree = [leaves]
    while len(tree[-1]) > 1:
        prev = tree[-1]
        layer = []
        for i in range(0, len(prev), 2):
            left  = prev[i]
            right = prev[i+1] if i+1 < len(prev) else prev[i]
            layer.append(sha256(left + right))
        tree.append(layer)
    return tree

def compute_proofs(tree: list[list[bytes]]) -> list[list[dict]]:
    """
    For each leaf index, generate a proof: a list of {sibling, direction}.
    direction is 'LEFT' or 'RIGHT' relative to the node.
    """
    proofs = []
    num_leaves = len(tree[0])
    for idx in range(num_leaves):
        proof = []
        index = idx
        for layer in tree[:-1]:
            # determine sibling index/direction
            if index % 2 == 0:
                sib_idx   = index + 1 if index + 1 < len(layer) else index
                direction = "RIGHT"
            else:
                sib_idx   = index - 1
                direction = "LEFT"
            proof.append({
                "sibling": layer[sib_idx].hex(),
                "direction": direction
            })
            index //= 2
        proofs.append(proof)
    return proofs

def main():
    parser = argparse.ArgumentParser(description="Generate Merkle metadata for OTA updates")
    parser.add_argument(
        "--firmware-dir",
        default="server/firmware",
        help="Directory containing *.bin firmware files"
    )
    parser.add_argument(
        "--output",
        default="server/metadata.json",
        help="Output metadata JSON path"
    )
    parser.add_argument(
        "--private-key",
        default="server/keys/ecdsa_priv.pem",
        help="Path to ECDSA private key (will be created if missing)"
    )
    parser.add_argument(
        "--public-key",
        default="server/keys/ecdsa_pub.pem",
        help="Path where ECDSA public key will be written"
    )
    args = parser.parse_args()

    # Ensure key directory exists
    os.makedirs(os.path.dirname(args.private_key), exist_ok=True)

    # Load or generate private key
    if os.path.exists(args.private_key):
        sk = SigningKey.from_pem(open(args.private_key, "rb").read())
    else:
        sk = SigningKey.generate(curve=NIST256p)
        with open(args.private_key, "wb") as f:
            f.write(sk.to_pem())

    # Export public key
    vk = sk.get_verifying_key()
    with open(args.public_key, "wb") as f:
        f.write(vk.to_pem())

    # Read and hash firmware files
    files = sorted(f for f in os.listdir(args.firmware_dir) if f.endswith(".bin"))
    leaves = []
    for fname in files:
        path = os.path.join(args.firmware_dir, fname)
        with open(path, "rb") as f:
            leaves.append(sha256(f.read()))

    # Build Merkle tree and proofs
    tree   = build_merkle(leaves)
    root   = tree[-1][0]
    proofs = compute_proofs(tree)

    # Sign the root hash
    signature = sk.sign(root)

    # Write metadata
    metadata = {
        "files": files,
        "leaves": [h.hex() for h in leaves],
        "proofs": proofs,
        "root_signature": signature.hex(),
        "curve": "NIST256p"
    }
    with open(args.output, "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"[+] Metadata written to {args.output}")
    print(f"[+] Public key written to {args.public_key}")

if __name__ == "__main__":
    main()
