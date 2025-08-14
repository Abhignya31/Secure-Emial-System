# 🔐 Secure Email System

A **Computer Networks project** implemented in **Python** that demonstrates secure email communication using **RSA encryption, digital signatures, and SHA-256 hashing**.  

The system allows users to log in (simulated), generate RSA key pairs, encrypt messages with a recipient’s public key, and digitally sign messages with their private key — ensuring **confidentiality, authenticity, and integrity** of communication.

---

## ✨ Features  

- 🔑 **RSA Key Generation** — Secure 2048-bit key pairs for encryption & signing  
- 📩 **Message Encryption** — Protects confidentiality using recipient's public key  
- ✍ **Digital Signature** — Ensures authenticity & integrity using sender's private key  
- 🛡 **SHA-256 Hashing** — Strong hashing for message signing  
- 💻 **Command-Line Interface** — Simple and lightweight  
- 🧪 **Demonstrates core Computer Networks security concepts**  

---

## 📚 Concepts Covered (Computer Networks Context)

This project demonstrates practical applications of **network security** concepts:  
- **Asymmetric Encryption (RSA)** for secure key exchange & confidentiality  
- **Digital Signatures** for authentication & non-repudiation  
- **Message Digest (SHA-256)** for data integrity  
- **Public/Private Key Management**  
- Simulated secure messaging workflow  

---

## 📦 Requirements  

- **Python 3.8+**  
- **PyCryptodome** library  

Install dependencies:  
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run
### Run the Secure Email System
```bash
python src/main.py
```

### You will be prompted for:
- Username & password (simulated login)
- Message to encrypt
- (Optional) Recipient’s public key

### The program will then:
- Generate an RSA key pair (if not already generated)
- Encrypt your message with the recipient’s public key
- Create a digital signature using your private key
- Display the encrypted message & signature

---

## 📂 Project Structure
```text
SecureEmailSystem/
│
├── src/
│   ├── main.py             # Main CLI logic & user interaction
│   └── crypto_utils.py     # Encryption, decryption, signing functions
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── screenshots/            # CLI screenshots
```
---

## ✅ Future Improvements
- 🖥 GUI version (Tkinter or PyQt)
- 🌐 Web interface (Flask/Django)
- 📂 Save/Load key files for persistent use
- 📧 Integrate SMTP for real email sending
- 📎 Support attachments
- 🔑 Stronger authentication with real database

---

## 🎯 Academic Use
- This project can be submitted as part of Computer Networks / Cybersecurity coursework to demonstrate:
- Encryption & Decryption flow in secure communication
- Role of digital signatures in authentication
- Hashing for message integrity
- Simulation of secure email transmission process
