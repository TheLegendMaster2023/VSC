#!/usr/bin/env python3
"""
Модуль модульного тестирования для GitLab CI/CD.
Лабораторная работа №5, СКФУ 2026.
Студент: Мухамеджанов Эльёр Тимурович, группа ПИН-б-о-24-1(2)
"""
import unittest

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 100), 0)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApp)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        exit(1)