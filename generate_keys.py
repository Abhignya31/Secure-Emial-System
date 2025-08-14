from crypto_utils import generate_key_pair

# Generate new key pair
private_key, public_key = generate_key_pair()

# Save to files
with open("keys/private.pem", "wb") as priv_file:
    priv_file.write(private_key)

with open("keys/public.pem", "wb") as pub_file:
    pub_file.write(public_key)

print("✅ Keys generated and saved to 'keys/' folder.")
