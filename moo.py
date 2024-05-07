"""Use of pycryptodome's encrypt and decrypt."""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter

class CbcMoo:
    """PascalCase"""
    def init(self, key, iv=None):
        self.key = key
        self.iv = iv or get_random_bytes(16)

    def encrypt(self, plaintext):
        """Encrypt"""
        cipher = AES.new(self.key, AES.MODE_ECB)
        ciphertext = b""
        previous_block = self.iv
        for i in range(0, len(plaintext), 16):
            block = plaintext[i:i + 16]
            xored_block = bytes(a ^ b for a, b in zip(block, previous_block))
            encrypted_block = cipher.encrypt(xored_block)
            ciphertext += encrypted_block
            previous_block = encrypted_block
        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypt"""
        cipher = AES.new(self.key, AES.MODE_ECB)
        plaintext = b""
        previous_block = self.iv
        for i in range(0, len(ciphertext), 16):
            block = ciphertext[i:i + 16]
            decrypted_block = cipher.decrypt(block)
            plaintext += bytes(a ^ b for a, b in zip(decrypted_block, previous_block))
            previous_block = block
        return plaintext

class CfbMoo:
    """PascalCase"""
    def init(self, key, iv=None):
        self.key = key
        self.iv = iv or get_random_bytes(16)

    def encrypt(self, plaintext):
        """encrypt"""
        cipher = AES.new(self.key, AES.MODE_ECB)
        ciphertext = b""
        previous_block = self.iv
        for i in range(0, len(plaintext), 16):
            encrypted_block = cipher.encrypt(previous_block)
            block = plaintext[i:i + 16]
            xored_block = bytes(a ^ b for a, b in zip(block, encrypted_block))
            ciphertext += xored_block
            previous_block = xored_block
        return ciphertext

    def decrypt(self, ciphertext):
        """decrypt"""
        cipher = AES.new(self.key, AES.MODE_ECB)
        plaintext = b""
        previous_block = self.iv
        for i in range(0, len(ciphertext), 16):
            encrypted_block = cipher.encrypt(previous_block)
            block = ciphertext[i:i + 16]
            xored_block = bytes(a ^ b for a, b in zip(block, encrypted_block))
            plaintext += xored_block
            previous_block = block
        return plaintext

class OfbMoo:
    """PascalCase"""
    def init(self, key, iv=None):
        self.key = key
        self.iv = iv or get_random_bytes(16)

    def encrypt(self, plaintext):
        """Encrypt"""
        cipher = AES.new(self.key, AES.MODE_ECB)
        ciphertext = b""
        previous_block = self.iv
        for i in range(0, len(plaintext), 16):
            encrypted_block = cipher.encrypt(previous_block)
            block = plaintext[i:i + 16]
            xored_block = bytes(a ^ b for a, b in zip(block, encrypted_block))
            ciphertext += xored_block
            previous_block = encrypted_block
        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypt"""
        return self.encrypt(ciphertext)

class CtrMoo:
    """PascalCase"""
    def init(self, key, nonce=None):
        self.key = key
        self.nonce = nonce or get_random_bytes(8)
        self.counter = Counter.new(128, initial_value=int.from_bytes(self.nonce, byteorder='big'), allow_wraparound=False)

    def encrypt(self, plaintext):
        """Encrypt"""
        cipher = AES.new(self.key, AES.MODE_CTR, counter=self.counter)
        ciphertext = cipher.encrypt(plaintext)
        return ciphertext

    def decrypt(self, ciphertext):
        """Decrypt"""
        return self.encrypt(ciphertext)
