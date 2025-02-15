![](https://img.shields.io/badge/SilverCrypt-v1.0.0-white.svg)
# SilverCrypt - Secure Password Manager

## 📌 About

In today's digital age, managing multiple passwords has become a challenge, especially when dealing with long and complex passwords for different online accounts. I needed a secure way to store and manage these passwords without relying on third-party services that could compromise my privacy.

That's how I developed **SilverCrypt** — a simple yet secure password manager that allows you to store, encrypt, and retrieve your passwords securely. Using a master password, SilverCrypt protects your sensitive data and gives you full control over your passwords.

---

## ✨ Features

- 🔒 **Secure Encryption**: All passwords are encrypted with strong algorithms and can only be decrypted with the master password.
- 💻 **Simple Terminal Interface**: A clean and easy-to-use interface to manage your passwords.
- ☁ **Google Drive Integration**: Option to securely store your encrypted passwords on Google Drive, allowing access from anywhere.
- 🔍 **Password Management**: Add, list, and retrieve your passwords securely.

---


## ❓ Why SilverCrypt?

I created **SilverCrypt** because managing passwords securely is more important than ever, and many existing password managers are cloud-based, which can pose a security risk. **SilverCrypt** was designed to give you full control over your data, ensuring everything remains private.


---

### 📟 Some required pip's:

**In your terminal, use these commands:**
```bash
$ pip install cryptography google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

---

## 🚀 Installation

### Prerequisites

Make sure you have **Python 3.12** or higher installed on your system.

### Steps:

**Follow these steps in your terminal:**
   ```bash
   $ cd ~/
   $ git clone https://github.com/ksferreira21/SilverCrypt -b main ~/.SilverCrypt
   $ alias silvercrypt='python3 ~/.SilverCrypt/main.py'
   $ echo "alias silvercrypt='python3 ~/.SilverCrypt/main.py'" >> ~/.bashrc
   ```
---

## ☁ Google Cloud Configuration

### Steps to Configure Google Drive API:

#### 1. Enable Google Drive API:
- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Create a new project or select an existing one.
- Enable **Google Drive API** for the project.

#### 2. Create a Service Account:
- In **IAM & Admin**, create a new service account.
- Assign the **Editor** or **Owner** role.

#### 3. Generate a Service Account Key:
- Go to the **Keys** tab.
- Click **Add Key** → **Create New Key** → Select **JSON**.
- Download the JSON file and save it in the `SilverCrypt` directory.

#### 4. Share the Google Drive Folder with the Service Account:
- Create a folder in Google Drive.
- Copy its **Folder ID** from the URL.
- Share the folder with the email address in your JSON key file. ⚠️

#### 5. Update the Configuration in drive_syn:
- Replace `SERVICE_ACCOUNT_FILE` with the path to your JSON key.
- Replace `FOLDER_ID` with your Google Drive folder ID.

---

## 🎩 How to Start **SilverCrypt**? 🛠️
**In your terminal:**

```bash
$ silvercrypt
```

- When you run **SilverCrypt** for the first time, a **master password** will be generated. This password will be used to encrypt and decrypt all your stored passwords (so don't lose it).

### Available Options:

1. **List your passwords**:
   - Select *"List stored passwords"*
   - View a list of all stored entries.
   - The .json file with your passwords on your Google Drive will have all encrypted passwords.

2. **Add a password**:
   - Select *"Add a password"*
   - Enter the service name (e.g., "Google", "Amazon")
   - Enter the password you want to store.

3. Visualize the folder in Google Drive, where you copied the ID, and the passwords.json file will be there. 

4. After that, enjoy using **SilverCrypt**! 👍

---

## 🤝 Contributing

If you wish to contribute to **SilverCrypt**, feel free to fork the repository and send a pull request. All help is welcome!

### Contribution Steps:

1. **Fork the repository**.

2. Create a new branch:
   ```bash
   $ git checkout -b feature-branch
   ```
3. Make your changes and commit:
   ```bash
   $ git commit -am 'Add new feature'
   ```
4. Push to the remote repository:
   ```bash
   $ git push origin feature-branch
   ```
5. Open a **Pull Request** on GitHub.

---