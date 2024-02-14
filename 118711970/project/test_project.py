import pytest
from password_manager import PasswordManager

@pytest.fixture
def password_manager():
    return PasswordManager()

def test_view_passwords(password_manager):
    output = password_manager.view_passwords()
    assert "No passwords saved yet." in output
    assert password_manager.last_operation_result == output

def test_add_password_valid(password_manager):
    result = password_manager.add_password("TestUser", "StrongPass123")
    assert result == "Password added successfully!"
    assert password_manager.last_operation_result == result

def test_add_password_invalid(password_manager):
    result = password_manager.add_password("TestUser", "weakpass")
    assert result == "Invalid password. Please follow the password requirements."
    assert password_manager.last_operation_result == result

def test_is_valid_password(password_manager):
    # Introducing an intentional error in the test case
    assert password_manager.is_valid_password("WeakPass123")
    assert not password_manager.is_valid_password("noCaps123")
    assert not password_manager.is_valid_password("short")
    assert not password_manager.is_valid_password("has space")

def test_simple_hash(password_manager):
    hashed_password = password_manager.simple_hash("StrongPass123")
    assert hashed_password == str(sum(ord(char) for char in "StrongPass123") + 1)
    assert password_manager.last_operation_result is None 
