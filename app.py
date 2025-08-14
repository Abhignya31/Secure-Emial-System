from flask import Flask, render_template, request
from crypto_utils import (
    user_login,
    generate_key_pair,
    encrypt_message,
    sign_message,
    verify_signature  # added verification function
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        message = request.form['message']
        recipient_key = request.form.get('recipient_key', '').strip()

        # Try to read uploaded file if no textarea key is provided
        if not recipient_key:
            key_file = request.files.get('recipient_key_file')
            if key_file and key_file.filename.endswith('.pem'):
                recipient_key = key_file.read().decode('utf-8')

        # Authenticate and process
        if user_login(username, password):
            private_key, public_key = generate_key_pair()

            # Use default key if recipient_key is still empty
            if not recipient_key.strip():
                recipient_key = None

            ciphertext = encrypt_message(message, recipient_key)
            signature = sign_message(message, private_key)

            return render_template("index.html",
                                   public_key=public_key.decode(),
                                   encrypted=ciphertext.hex(),
                                   signature=signature.hex())
        else:
            return render_template("index.html", error="❌ Invalid credentials")

    return render_template("index.html")


@app.route('/verify', methods=['GET', 'POST'])
def verify_signature():
    if request.method == 'POST':
        message = request.form.get('message')
        signature_hex = request.form.get('signature')
        public_key_pem = request.form.get('public_key')

        # Handle uploaded file if no key pasted
        if not public_key_pem and 'public_key_file' in request.files:
            file = request.files['public_key_file']
            if file and file.filename.endswith('.pem'):
                public_key_pem = file.read().decode()

        try:
            # Convert hex string back to bytes
            signature = bytes.fromhex(signature_hex)
            public_key = serialization.load_pem_public_key(public_key_pem.encode())

            # Verify
            public_key.verify(
                signature,
                message.encode(),
                padding.PKCS1v15(),
                hashes.SHA256()
            )
            return render_template('verify.html', result={"verified": True})
        except Exception as e:
            print("Verification Error:", str(e))
            return render_template('verify.html', result={"verified": False})

    # Only GET request, don't show fail by default
    return render_template('verify.html')


if __name__ == "__main__":
    app.run(debug=True)
