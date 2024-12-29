import hashlib
import os
from typing import Optional

class Hash:
    # Function to hash a password
    @staticmethod
    def hash_password(password: str, salt: Optional[bytes] = None) -> str:
        if not salt:
            salt = os.urandom(16)  # Generate a random 16-byte salt
        password_salt = salt + password.encode("utf-8")
        hashed_password = hashlib.sha256(password_salt).hexdigest()
        return f"{salt.hex()}${hashed_password}"

    # Function to verify the password
    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        salt, stored_hash = hashed_password.split("$")
        salt = bytes.fromhex(salt)
        return hashlib.sha256(salt + password.encode("utf-8")).hexdigest() == stored_hash