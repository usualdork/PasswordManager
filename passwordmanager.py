import hashlib
import secrets
import logging
import uuid
import tkinter as tk
from tkinter import messagebox
import pyperclip

class PasswordManager:
    def __init__(self):
        self.passwords = {}
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def add_password(self, website, username, password):
        identifier = str(uuid.uuid4())[:8]  # Generate a unique identifier
        salt = secrets.token_hex(8)  # Generate a random salt
        hashed_password = self._hash_password(password, salt)
        self.passwords[identifier] = (website, username, hashed_password, salt, password)
        self.logger.info(f"Password added for {username} at {website} with identifier {identifier}")
        return identifier

    def get_credentials(self, identifier):
        if identifier in self.passwords:
            website, username, _, _, password = self.passwords[identifier]
            return website, username, password
        else:
            return None

    def delete_credentials(self, identifier):
        if identifier in self.passwords:
            del self.passwords[identifier]
            return True
        else:
            return False

    def _hash_password(self, password, salt):
        # Hash the password with SHA-256 and the salt
        hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
        return hashed_password

    def display_all_credentials(self):
        websites = []
        if self.passwords:
            for identifier, (website, _, _, _, _) in self.passwords.items():
                websites.append(website)
        return websites


class PasswordManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")

        # Set window dimensions
        self.master.geometry("600x400")

        self.manager = PasswordManager()

        # Set background color
        self.master.configure(bg="#282828")

        # Create main frame
        self.main_frame = tk.Frame(master, bg="#282828")
        self.main_frame.pack(expand=True, fill="both")

        # Create label
        self.label = tk.Label(self.main_frame, text="Password Manager Menu", font=("Arial", 16), bg="#282828", fg="#FFFFFF")
        self.label.pack(pady=10)

        # Create buttons
        self.add_button = tk.Button(self.main_frame, text="Add new credentials", command=self.add_credentials, font=("Arial", 12), bg="#484848", fg="#FFFFFF", bd=0)
        self.add_button.pack(pady=5, padx=20, fill="x")

        self.retrieve_button = tk.Button(self.main_frame, text="Retrieve credentials", command=self.retrieve_credentials, font=("Arial", 12), bg="#484848", fg="#FFFFFF", bd=0)
        self.retrieve_button.pack(pady=5, padx=20, fill="x")

        self.delete_button = tk.Button(self.main_frame, text="Delete credentials", command=self.delete_credentials, font=("Arial", 12), bg="#484848", fg="#FFFFFF", bd=0)
        self.delete_button.pack(pady=5, padx=20, fill="x")

        self.display_button = tk.Button(self.main_frame, text="Display all credentials", command=self.display_credentials, font=("Arial", 12), bg="#484848", fg="#FFFFFF", bd=0)
        self.display_button.pack(pady=5, padx=20, fill="x")

        self.exit_button = tk.Button(self.main_frame, text="Exit", command=master.quit, font=("Arial", 12), bg="#484848", fg="#FFFFFF", bd=0)
        self.exit_button.pack(pady=5, padx=20, fill="x")

        # Set button hover effects
        self.hover_effect()

    def hover_effect(self):
        # Button hover effects
        buttons = [self.add_button, self.retrieve_button, self.delete_button, self.display_button, self.exit_button]
        for button in buttons:
            button.bind("<Enter>", self.on_enter)
            button.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        event.widget.config(bg="#606060")

    def on_leave(self, event):
        event.widget.config(bg="#484848")

    def add_credentials(self):
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Add New Credentials")

        # Set background color
        self.add_window.configure(bg="#282828")

        tk.Label(self.add_window, text="Website name:", font=("Arial", 12), bg="#282828", fg="#FFFFFF").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(self.add_window, text="Username:", font=("Arial", 12), bg="#282828", fg="#FFFFFF").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(self.add_window, text="Password:", font=("Arial", 12), bg="#282828", fg="#FFFFFF").grid(row=2, column=0, padx=5, pady=5)

        self.website_entry = tk.Entry(self.add_window, font=("Arial", 12))
        self.website_entry.grid(row=0, column=1, padx=5, pady=5)
        self.username_entry = tk.Entry(self.add_window, font=("Arial", 12))
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)
        self.password_entry = tk.Entry(self.add_window, show="*", font=("Arial", 12))
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        add_button = tk.Button(self.add_window, text="Add", command=self.add_credentials_action, font=("Arial", 12), bg="#484848", fg="#FFFFFF", bd=0)
        add_button.grid(row=3, columnspan=2, pady=5)

    def add_credentials_action(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        identifier = self.manager.add_password(website, username, password)
        messagebox.showinfo("Success", f"Your identifier for {website} is: {identifier}  & The identifier has been copied to clipboard")
        pyperclip.copy(identifier)  # Copy identifier to clipboard
        self.add_window.destroy()

    def retrieve_credentials(self):
        self.retrieve_window = tk.Toplevel(self.master)
        self.retrieve_window.title("Retrieve Credentials")

        # Set background color
        self.retrieve_window.configure(bg="#282828")

        tk.Label(self.retrieve_window, text="Enter identifier:", font=("Arial", 12), bg="#282828", fg="#FFFFFF").grid(row=0, column=0, padx=5, pady=5)
        self.identifier_entry = tk.Entry(self.retrieve_window, font=("Arial", 12))
        self.identifier_entry.grid(row=0, column=1, padx=5, pady=5)

        retrieve_button = tk.Button(self.retrieve_window, text="Retrieve", command=self.retrieve_credentials_action, font=("Arial", 12), bg="#484848", fg="#FFFFFF", bd=0)
        retrieve_button.grid(row=1, columnspan=2, pady=5)

    def retrieve_credentials_action(self):
        identifier = self.identifier_entry.get()
        stored_info = self.manager.get_credentials(identifier)
        if stored_info:
            website, username, password = stored_info
            messagebox.showinfo("Credentials", f"Website: {website}, Username: {username}, Password: {password}")
        else:
            messagebox.showinfo("Error", "Invalid identifier.")
        self.retrieve_window.destroy()

    def delete_credentials(self):
        self.delete_window = tk.Toplevel(self.master)
        self.delete_window.title("Delete Credentials")

        # Set background color
        self.delete_window.configure(bg="#282828")

        tk.Label(self.delete_window, text="Enter identifier:", font=("Arial", 12), bg="#282828", fg="#FFFFFF").grid(row=0, column=0, padx=5, pady=5)
        self.delete_entry = tk.Entry(self.delete_window, font=("Arial", 12))
        self.delete_entry.grid(row=0, column=1, padx=5, pady=5)

        delete_button = tk.Button(self.delete_window, text="Delete", command=self.delete_credentials_action, font=("Arial", 12), bg="#484848", fg="#FFFFFF", bd=0)
        delete_button.grid(row=1, columnspan=2, pady=5)

    def delete_credentials_action(self):
        identifier = self.delete_entry.get()
        if self.manager.delete_credentials(identifier):
            messagebox.showinfo("Success", "Credentials deleted successfully.")
        else:
            messagebox.showinfo("Error", "Invalid identifier.")
        self.delete_window.destroy()

    def display_credentials(self):
        self.display_window = tk.Toplevel(self.master)
        self.display_window.title("Display All Credentials")

        # Set background color
        self.display_window.configure(bg="#282828")

        credentials_info = self.manager.display_all_credentials()
        for website in credentials_info:
            tk.Label(self.display_window, text=website, font=("Arial", 12), bg="#282828", fg="#FFFFFF").pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerGUI(root)
    root.mainloop()
