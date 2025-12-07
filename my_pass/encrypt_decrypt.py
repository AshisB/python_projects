import base64
import json
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import hashlib


class Encryption:
    def __init__(self):
        self.master_password = None

    def encrypt(self, data: dict,master_password) -> str:
        # Generate salt and derive key
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
        fernet = Fernet(key)

        # Encrypt
        json_str = json.dumps(data).encode()
        encrypted = fernet.encrypt(json_str)

        # Return salt + encrypted as base64
        combined = salt + encrypted
        return base64.b64encode(combined).decode()

    def decrypt(self, encrypted_str: str,master_password) -> dict:
        # Decode base64
        combined = base64.b64decode(encrypted_str.encode())

        # Extract salt and encrypted data
        salt = combined[:16]
        encrypted = combined[16:]

        # Derive key and decrypt
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
        fernet = Fernet(key)

        decrypted = fernet.decrypt(encrypted)
        return json.loads(decrypted.decode())

    def save_to_file(self, data, filename="passwords.enc"):  # ✅ Fixed name
        encrypted_string = self.encrypt(data,self.master_password)
        with open(filename, "w") as f:
            f.write(encrypted_string)
        print(f"✅ Saved to {filename}")

    def load_from_file(self, filename="passwords.enc"):  # ✅ Fixed name
        if not os.path.exists(filename):
            return {}

        with open(filename, "r") as f:
            encrypted_string = f.read()

        return self.decrypt(encrypted_string,self.master_password)

    def create_master_hash(self,master_password: str):
        """Create and save hash of master password"""
        password_hash = hashlib.sha256(master_password.encode()).hexdigest()
        with open("master.hash", "w") as f:
            f.write(password_hash)

    def verify_master_hash(self,master_password: str) -> bool:
        """Verify against stored hash"""
        if not os.path.exists("master.hash"):
            return False  # No master password set yet

        with open("master.hash", "r") as f:
            stored_hash = f.read().strip()

        entered_hash = hashlib.sha256(master_password.encode()).hexdigest()
        return entered_hash == stored_hash