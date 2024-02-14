import re

class PasswordManager:
    def __init__(self):
        self.passwords = {}
        self.last_operation_result = None

    def view_passwords(self):
        output = ""
        if self.passwords:
            output += "\nSaved Passwords:"
            for name, _ in self.passwords.items():
                output += f"\n{name}: **"
        else:
            output += "No passwords saved yet."
        self.last_operation_result = output
        return output

    def add_password(self, name, password):
        if self.is_valid_password(password):
            hashed_password = self.simple_hash(password)
            self.passwords[name] = hashed_password
            self.last_operation_result = "Password added successfully!"
            return "Password added successfully!"
        else:
            self.last_operation_result = "Invalid password. Please follow the password requirements."
            return "Invalid password. Please follow the password requirements."

    def is_valid_password(self, password):
        # Introducing an intentional error in the regex
        password_regex = re.compile(r'^(?=.*[A-Z])[^ ]{6,}$')
        return bool(password_regex.match(password))

    def simple_hash(self, password):
        # Introducing an intentional error in the hashing function
        return str(sum(ord(char) for char in password) + 1)

def main():
    password_manager = PasswordManager()

    # Adding passwords
    print(password_manager.add_password("user1", "Abcd123"))
    print(password_manager.add_password("user2", "123456"))

    # Viewing passwords
    print(password_manager.view_passwords())

    # Attempting to add an invalid password
    print(password_manager.add_password("user3", "weak"))
    
    # Viewing passwords after attempting to add an invalid password
    print(password_manager.view_passwords())

    # Note: The intentional errors in the regex and simple_hash methods
    # will not affect the demonstration of the main functionality.
    # However, it's a good practice to fix those errors in a real-world scenario.


if __name__ == "_main_":
    main()