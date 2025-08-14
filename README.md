# 🔐 Secure Email System

A simple command-line tool built in Python that allows users to:
- Login (simulated)
- Generate RSA key pairs
- Encrypt messages using a public key
- Digitally sign messages using a private key

All encryption and signing operations are done using PyCryptodome (RSA + SHA256).

---

## 🛠️ Features

- 🔑 RSA Key Generation (2048-bit)
- 🔐 Message Encryption with recipient's public key
- ✍️ Message Signing with sender's private key
- 💻 Simple command-line interface

---

## 📦 Requirements

- Python 3.8+
- PyCryptodome

Install with:
```bash
pip install -r requirements.txt

---

## 🚀 How to Run

```bash
Copy code
python src/main.py

- You’ll be prompted for:

1) Username and password (for simulated login)
2) A message to encrypt
3) Optional recipient's public key

---

## 📁 Project Structure

```bash
SecureEmailSystem/
├── src/
│   ├── main.py             # Main CLI script
│   └── crypto_utils.py     # All encryption/signature functions
├── requirements.txt        # Python dependencies
├── README.md               # You're reading it

---

## 📷 Screenshots

Here’s a sample run of the command-line Secure Email System:

### 🔐 Login and Key Generation
![Login and Key Generation](screenshots/cli-login.png)

### ✉️ Message Encryption and Signature
![Encryption and Signature](screenshots/cli-encryption.png)
---

## ✅ To-Do / Future Improvements

- GUI version using Tkinter
- Web version using Flask
- Save/load key files
- Add basic email sending (SMTP)
- Attachments support
- Real database authentication


