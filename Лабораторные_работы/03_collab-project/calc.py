#!/usr/bin/env python3
"""
Модуль калькулятора для совместного проекта collab-project.
Лабораторная работа №3, СКФУ 2026.
Студент: Мухамеджанов Эльёр Тимурович, группа ПИН-б-о-24-1(2)
"""

def add(a: float, b: float) -> float:
    """Сложение двух чисел."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитание b из a."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Умножение двух чисел."""
    return a * b

def divide(a: float, b: float) -> float:
    """Деление a на b с проверкой деления на ноль."""
    if b == 0:
        raise ValueError("Ошибка: Деление на ноль невозможно!")
    return a / b

if __name__ == "__main__":
    print("Калькулятор запущен.")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"3 * 5 = {multiply(3, 5)}")
    print(f"15 / 3 = {divide(15, 3)}")