from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

def user_login(username, password):
    hashed_password = SHA256.new(password.encode()).hexdigest()
    # In real systems, compare hashed_password with stored hash
    return True  # For demo purposes

def generate_key_pair():
    private_key = RSA.generate(2048)
    public_key = private_key.publickey()
    return private_key.export_key(), public_key.export_key()

def encrypt_message(message, recipient_public_key=None):
    if recipient_public_key:
        # Clean up newline characters from textarea input
        recipient_public_key = recipient_public_key.replace('\\n', '\n').strip()
    else:
        # Load default public key from file
        with open("keys/public.pem", "rb") as f:
            recipient_public_key = f.read()

    recipient_key = RSA.import_key(recipient_public_key)
    cipher = PKCS1_OAEP.new(recipient_key)
    ciphertext = cipher.encrypt(message.encode('utf-8'))
    return ciphertext

def sign_message(message, sender_private_key):
    private_key = RSA.import_key(sender_private_key)
    signer = pkcs1_15.new(private_key)
    signature = signer.sign(SHA256.new(message.encode()))
    return signature

def verify_signature(message, signature_hex, sender_public_key):
    try:
        public_key = RSA.import_key(sender_public_key)
        verifier = pkcs1_15.new(public_key)
        hash_value = SHA256.new(message.encode())
        signature_bytes = bytes.fromhex(signature_hex)
        verifier.verify(hash_value, signature_bytes)
        return True
    except (ValueError, TypeError):
        return False
