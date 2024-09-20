from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Step 1: Generate a random key (16 bytes for AES-128)
key = get_random_bytes(16)

# Step 2: Create a cipher object using the key and set the mode (AES.MODE_CBC)
cipher = AES.new(key, AES.MODE_CBC)

# Step 3: The data to be encrypted (plaintext)
data = b'Hello, this is AES encryption!'

# Step 4: Padding the data to make it a multiple of AES block size (16 bytes)
padded_data = pad(data, AES.block_size)

# Step 5: Encrypt the padded data
ciphertext = cipher.encrypt(padded_data)

# Step 6: Print the ciphertext
print("Ciphertext:", ciphertext)

# Step 7: Decrypting
cipher_dec = AES.new(key, AES.MODE_CBC, cipher.iv)
decrypted_data = unpad(cipher_dec.decrypt(ciphertext), AES.block_size)

# Step 8: Print decrypted data (plaintext)
print("Decrypted Data:", decrypted_data.decode())
