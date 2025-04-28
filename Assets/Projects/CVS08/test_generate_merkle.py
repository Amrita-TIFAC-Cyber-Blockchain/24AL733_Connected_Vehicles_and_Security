import os
import sys
import json
import hashlib
import subprocess
import tempfile
import pathlib
import pytest

# Ensure the server/ directory is on PYTHONPATH
HERE = pathlib.Path(__file__).parent.resolve()
PROJECT_ROOT = HERE.parent.parent.resolve()
SERVER_DIR = PROJECT_ROOT / "server"
sys.path.insert(0, str(SERVER_DIR))

import generate_merkle
from ecdsa import VerifyingKey

def compute_sha256_hexdigest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

@pytest.mark.usefixtures("tmp_path")
def test_generate_merkle_and_verify(tmp_path):
    # 1. Create a fake firmware directory
    fw_dir = tmp_path / "firmware"
    fw_dir.mkdir()
    # Create two dummy firmware files
    (fw_dir / "ecuA.bin").write_bytes(b"alpha-firmware")
    (fw_dir / "ecuB.bin").write_bytes(b"beta-firmware")

    # 2. Define paths for metadata & keys
    metadata_path = tmp_path / "metadata.json"
    keys_dir      = tmp_path / "keys"
    priv_path     = keys_dir / "priv.pem"
    pub_path      = keys_dir / "pub.pem"
    keys_dir.mkdir()

    # 3. Run the generate_merkle script
    subprocess.run([
        sys.executable,
        str(SERVER_DIR / "generate_merkle.py"),
        "--firmware-dir", str(fw_dir),
        "--output",       str(metadata_path),
        "--private-key",  str(priv_path),
        "--public-key",   str(pub_path),
    ], check=True)

    # 4. Load metadata
    meta = json.loads(metadata_path.read_text())
    assert meta["files"] == ["ecuA.bin", "ecuB.bin"]

    # 5. Check leaves match expected SHA256 hex digests
    expected = [
        compute_sha256_hexdigest(b"alpha-firmware"),
        compute_sha256_hexdigest(b"beta-firmware")
    ]
    assert meta["leaves"] == expected

    # 6. Rebuild Merkle root
    leaf_bytes = [bytes.fromhex(h) for h in meta["leaves"]]
    tree = generate_merkle.build_merkle(leaf_bytes)
    root = tree[-1][0]

    # 7. Verify ECDSA signature on root
    signature = bytes.fromhex(meta["root_signature"])
    vk = VerifyingKey.from_pem(pub_path.read_bytes())
    assert vk.verify(signature, root)

    # 8. Verify each proof recomputes the same root
    proofs = meta["proofs"]
    for idx, proof in enumerate(proofs):
        # start with leaf
        h = leaf_bytes[idx]
        for step in proof:
            sib = bytes.fromhex(step["sibling"])
            if step["direction"] == "RIGHT":
                h = hashlib.sha256(h + sib).digest()
            else:
                h = hashlib.sha256(sib + h).digest()
        # h should equal root
        assert h == root
