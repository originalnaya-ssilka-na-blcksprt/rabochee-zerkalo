import random
import string
import secrets

def generate_password(length=12, include_symbols=True, include_numbers=True, include_uppercase=True, include_lowercase=True):
    """Генерирует безопасный пароль с настраиваемыми параметрами"""
    characters = ""
    
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not characters:
        return "Ошибка: не выбрано ни одного типа символов"
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Пример использования
print("Простые пароли:")
for i in range(3):
    print(f"Пароль {i+1}: {generate_password(8)}")

print("\nСложные пароли:")
for i in range(3):
    print(f"Пароль {i+1}: {generate_password(16, include_symbols=True)}")
