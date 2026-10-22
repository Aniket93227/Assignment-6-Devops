"""Standard-library unit tests for app.py."""
import unittest
from app import greeting


class GreetingTests(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greeting(), "Hello, Jenkins!")

    def test_named_greeting(self):
        self.assertEqual(greeting("GitHub"), "Hello, GitHub!")


if __name__ == "__main__":
    unittest.main(verbosity=2)
