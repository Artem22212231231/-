"""
Модуль валидации ввода.
"""

import re


def validate_password_settings(settings: dict) -> list:
    """
    Проверяет корректность настроек генерации пароля.
    Возвращает список ошибок (пустой, если всё верно).
    settings — словарь с ключами: length, use_uppercase, use_digits, use_special
    """
    errors = []

    # Длина
    length = settings.get('length')
    if not isinstance(length, int) or not (6 <= length <= 128):
        errors.append("Длина пароля должна быть целым числом от 6 до 128.")

    # Булевы флаги
    for key in ['use_uppercase', 'use_digits', 'use_special']:
        if not isinstance(settings.get(key), bool):
            errors.append(f"Параметр '{key}' должен быть булевым значением (True/False).")

    # Хотя бы один тип символов
    if not any([settings.get('use_uppercase', True),
                settings.get('use_digits', True),
                settings.get('use_special', True)]):
        errors.append("Должен быть выбран хотя бы один дополнительный набор символов.")

    return errors


def validate_password_name(name: str) -> str | None:
    """Проверяет имя пароля. Возвращает сообщение об ошибке или None."""
    if not name or not name.strip():
        return "Имя пароля не может быть пустым."
    if len(name.strip()) > 50:
        return "Имя пароля должно быть не длиннее 50 символов."
    if not re.match(r'^[A-Za-zА-Яа-я0-9 _-]+$', name.strip()):
        return "Имя может содержать только буквы, цифры, пробелы, дефисы и подчёркивания."
    return None
