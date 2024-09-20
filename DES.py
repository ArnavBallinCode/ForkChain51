from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Step 1: Generate a random key (DES uses a 64-bit key, but only 56 bits are used for encryption)
key = get_random_bytes(8)  # 8 bytes (64 bits) for DES key

# Step 2: Create a DES cipher object with the key in ECB mode
cipher = DES.new(key, DES.MODE_ECB)

# Step 3: Data to be encrypted (must be in multiples of 8 bytes)
data = b"DES is old!"

# Step 4: Padding the data to make it a multiple of 8 bytes
padded_data = pad(data, DES.block_size)

# Step 5: Encrypt the data
ciphertext = cipher.encrypt(padded_data)

# Step 6: Print the ciphertext
print("Ciphertext:", ciphertext)

# Step 7: Decrypting the ciphertext
decrypted_data = cipher.decrypt(ciphertext)

# Step 8: Unpad the decrypted dataa
unpadded_data = unpad(decrypted_data, DES.block_size)


# Step 9: Print the decrypted (original) data
print("Decrypted Data:", unpadded_data.decode())

