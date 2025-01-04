# Password Manager

A simple and efficient password manager built using Python's Tkinter library. This app helps you securely store and manage your passwords, generate strong random passwords, and retrieve saved credentials.

---

## Features

- **Password Generator**: Create strong, random passwords with a mix of letters, numbers, and symbols.
- **Credential Storage**: Save website, email, and password details to a JSON file (`file.json`).
- **Search Functionality**: Retrieve stored credentials for a specific website.
- **User-Friendly Interface**: Designed with an intuitive GUI for ease of use.

---

## Prerequisites

- **Python 3.x**
- Libraries:
  - `tkinter` (standard library)
  - `json`
  - `random`

---

## How to Run

1. Clone or download the repository.
   ```bash
   git clone https://github.com/Pooja389/password-app.git
   ```
3. Ensure that `pass_generator.py` and `pass1.png` are in the same folder.
4. Open a terminal/command prompt, navigate to the folder, and run the script:

   ```bash
   python pass_generator.py
   ```
## How It Works

1. **Adding Credentials**:
   - Enter the **Website** name in the "Website" field.
   - Provide your **Email** or username in the "Email" field (a default email is pre-filled).
   - Enter your **Password** manually or use the **Generate Pass** button to create a strong, random password.
   - Click the **Add** button to save the credentials. The data is securely stored in a JSON file (`file.json`).

2. **Generating Passwords**:
   - Click the **Generate Pass** button to create a strong password.
   - The password will be a combination of random letters, numbers, and symbols.
   - The generated password will automatically appear in the "Password" field.

3. **Searching for Credentials**:
   - Enter the **Website** name in the "Website" field.
   - Click the **Search** button to find credentials for the specified website.
   - If the website exists in the database, a popup will display the associated email and password.
   - If no data is found, you will be notified that no credentials exist for the given website.

4. **Auto-Email Input**:
   - The "Email" field is pre-filled with a default email (`abc@gmail.com`).
   - You can replace it with your preferred email before saving the data.

This app simplifies password management and ensures your credentials are securely stored and easily accessible.



