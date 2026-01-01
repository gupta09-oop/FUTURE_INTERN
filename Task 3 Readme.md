🔐 Secure File Upload & Download Portal (AES Encryption)

A secure web application built using Python Flask that allows users to encrypt files before upload, store only encrypted data, and decrypt encrypted files securely via a web interface.

This project demonstrates secure file handling, cryptography fundamentals, and backend web development.

🚀 Features

🔐 AES-256 Encryption at Rest

📤 Upload & encrypt files before storage

📥 Download encrypted files (.enc)

🔓 Decrypt encrypted files through web UI

🗝 Secure key management using environment variables

🖥 Simple and user-friendly web interface

🛡 No plaintext data stored on disk

🧠 How It Works

Upload & Encrypt

User uploads a file

File is encrypted using AES-256 (CBC mode)

Encrypted data is stored in the uploads/ directory

Download Encrypted File

User downloads the encrypted version of the file (.enc)

Decrypt File

User uploads the encrypted file

Server decrypts it using the same AES key

Original file is returned securely

⚠️ Decryption only works for files encrypted by this portal.

🛠 Tech Stack

Backend: Python, Flask

Cryptography: PyCryptodome (AES-256)

Frontend: HTML, CSS, Jinja2

Security: Environment variables (python-dotenv)

Version Control: Git & GitHub

📂 Project Structure
Task3/
├── app.py
├── crypto_utils.py
├── templates/
│   └── index.html
├── uploads/          # ignored in Git
├── .env              # ignored in Git
├── .gitignore
├── README.md
└── requirements.txt

▶️ How to Run Locally
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Create .env File
AES_SECRET=Your32ByteSecretKeyHere!!!!


⚠️ Key must be exactly 32 bytes.

3️⃣ Run the Application
python app.py

4️⃣ Open in Browser
http://127.0.0.1:5000

🔐 Security Notes

Uses AES-256-CBC with a random IV per file

IV is prepended to ciphertext

No encryption keys are hardcoded

.env and uploads/ are excluded via .gitignore

Prevents double-decryption and invalid input handling

🧪 Example Use Case

Upload confidential documents securely

Store encrypted backups

Demonstrate cryptography concepts

Practice secure backend development

📌 Learning Outcomes

Cryptographic encryption & decryption

Secure file handling

Flask routing & templating

Debugging real-world crypto issues

Secure Git practices

Backend + frontend integration

👤 Author

Kshitij Gupta
Cybersecurity Student | Secure Web Applications | Cryptography

⭐ Future Improvements

Upgrade to AES-GCM (authenticated encryption)

Add user authentication (JWT / Login)

File integrity verification

Cloud deployment (Render / Railway)

Improved UI with Bootstrap
