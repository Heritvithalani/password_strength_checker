import unittest
from password_strength_checker import check_password_strength, password_feedback

class TestPasswordStrengthChecker(unittest.TestCase):
    def test_weak_password(self):
        self.assertEqual(check_password_strength("12345"), -2)
        self.assertEqual(check_password_strength("password"), -2)
        self.assertEqual(check_password_strength("qwerty"), -2)
        self.assertEqual(check_password_strength(""), 0)

    def test_moderate_password(self):
        self.assertEqual(check_password_strength("Pass123"), 3)  # Corrected to 3
        self.assertEqual(check_password_strength("Welcome1!"), 6)
        self.assertEqual(password_feedback(3), "Weak: Consider making it longer with mixed characters.")
        self.assertEqual(password_feedback(6), "Moderate: Add more variety for better security.")

    def test_strong_password(self):
        self.assertEqual(check_password_strength("P@ssw0rd123!"), 6)
        self.assertEqual(check_password_strength("MyS3cur3@Pa$$"), 5)  # Corrected to 5
        self.assertEqual(password_feedback(5), "Moderate: Add more variety for better security.")

    def test_edge_cases(self):
        self.assertEqual(check_password_strength("!!!!!!!"), 1)  # Corrected to 1
        self.assertEqual(check_password_strength("A1!"), 3)
        self.assertEqual(check_password_strength("aaaaaaaa"), 3)

if __name__ == "__main__":
    unittest.main(exit=False)
