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
        
        password_regex = re.compile(r'^(?=.*[A-Z])[^ ]{6,}$')
        return bool(password_regex.match(password))

    def simple_hash(self, password):

        return str(sum(ord(char) for char in password) + 1)

def main():
    password_manager = PasswordManager()


    print(password_manager.add_password("user1", "Abcd123"))
    print(password_manager.add_password("user2", "123456"))

    print(password_manager.view_passwords())


    print(password_manager.add_password("user3", "weak"))

    print(password_manager.view_passwords())




if __name__ == "__main__":
    main()
