from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()

# Initialize Fernet cipher with the key
cipher = Fernet(key)

# Encrypt data
data = b"Sensitive data to be encrypted"
encrypted_data = cipher.encrypt(data)

# Decrypt data
decrypted_data = cipher.decrypt(encrypted_data)
print(decrypted_data.decode())