"""
Пользователь - имеет логин и пароль, а так же календарь.
у пользователя есть итендифекатор начинающийся с @
"""
import hashlib
import unittest
from Calendar import Calendar  # Импорт класса Calendar из модуля Calendar


def hash_password(password):
    # Метод для хеширования пароля
    return hashlib.sha256(password.encode()).hexdigest()


class User:
    def __init__(self, login: object, password: object) -> object:
        # Инициализация пользователя с логином и паролем
        self.login = login
        self.password = hash_password(password)  # Хеширование пароля
        self.calendar = Calendar(self)  # Создание календаря пользователя
        self.identifier = '@' + str(id(self))  # Генерация уникального идентификатора пользователя


class TestUser(unittest.TestCase):
    def setUp(self):
        # Устанавливаем начальные параметры перед каждым тестом
        self.user = User('test_user', 'password123')

    def test_user_attributes(self):
        # Проверяем основные атрибуты пользователя
        self.assertEqual(self.user.login, 'test_user')
        self.assertNotEqual(self.user.password, 'password123')  # Пароль должен быть захеширован
        self.assertIsInstance(self.user.calendar, Calendar)  # Пользователь должен иметь свой календарь
        self.assertTrue(self.user.identifier.startswith('@'))  # Идентификатор должен начинаться с "@"

    def test_password_hashing(self):
        # Проверяем корректность хеширования пароля
        hashed_password = hash_password("password123")
        self.assertNotEqual(hashed_password, 'password123')  # Захешированный пароль не должен совпадать с исходным


if __name__ == "__main__":
    unittest.main()
