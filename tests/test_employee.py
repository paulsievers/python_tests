import unittest
from app.employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1 = Employee("John", "Smith", 50000)
        self.emp_2 = Employee("Susan", "Anderson", 60000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, "John.Smith@company.com")
        self.assertEqual(self.emp_2.email, "Susan.Anderson@company.com") #is this line too long yets
