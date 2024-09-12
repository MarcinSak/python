import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        result = cap.cap_test('python')
        self.assertEqual(result, "Python")
    def test_many_words(self):
        result = cap.cap_test("monthy python")
        self.assertEqual(result, "Monthy Python")

if __name__ == "__main__":
    unittest.main()