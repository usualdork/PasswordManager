# PasswordManager

Password Manager is a simple Python application built using the Tkinter library for creating a graphical user interface (GUI). It allows users to securely store, retrieve, and manage their website credentials.

## Features
- Add New Credentials: Users can add new website credentials including website name, username, and password.
- Retrieve Credentials: Users can retrieve stored credentials by entering the corresponding identifier.
- Delete Credentials: Users can delete stored credentials by entering the corresponding identifier.
- Display All Credentials: Users can view a list of all stored websites for quick reference.
- Secure Storage: Passwords are securely hashed using SHA-256 and stored with unique identifiers.

<p align="center">
  <img src="https://github.com/usualdork/PasswordManager/assets/131380708/56486bdc-489f-41d2-a852-260246e674b5" alt="Start window">
</p>

## How to Use

1. Add New Credentials:
- Click on the "Add new credentials" button.
- Enter the website name, username, and password.
- Click the "Add" button to store the credentials.
- A unique identifier will be created for the credentials and will be automatically copied to the clipboard.

<p align="center">
  <img src="https://github.com/usualdork/PasswordManager/assets/131380708/62d87383-f48e-4f97-8fac-3a42d861d38f" alt="Start window">
</p>

2. Retrieve Credentials:
- Click on the "Retrieve credentials" button.
- Enter the identifier associated with the desired credentials.
- Click the "Retrieve" button to view the website, username, and password.

<p align="center">
  <img src="https://github.com/usualdork/PasswordManager/assets/131380708/b586ab60-4691-43da-9870-67539edb6727" alt="Start window">
</p>
 
3. Delete Credentials:
- Click on the "Delete credentials" button.
- Enter the identifier associated with the credentials to be deleted.
- Click the "Delete" button to remove the credentials.

<p align="center">
  <img src="https://github.com/usualdork/PasswordManager/assets/131380708/20417e94-fbce-4e6a-9678-d6d8ffa40994" alt="Start window">
</p>

4. Display All Credentials:
- Click on the "Display all credentials" button to view a list of all stored website names.

<p align="center">
  <img src="https://github.com/usualdork/PasswordManager/assets/131380708/5d2f861b-50f6-4b84-99b8-cb92068bc000" alt="Start window">
</p>

## Installation
1. Clone the repository:
`git clone https://github.com/usualdork/PasswordManager.git`
2. Install the required dependencies:
`pip install pyperclip`
3. Run the application:
`python PasswordManager.py`

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
`https://github.com/usualdork/PasswordManager/blob/main/LICENSE`
