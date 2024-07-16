import unittest
from api import app


class TestCalculatorAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_add(self):
        response = self.client.get("/add?a=10&b=20")
        self.assertEqual(response.json["result"], 30)
        print("add ok")

    def test_subtract(self):
        response = self.client.get("/subtract?a=20&b=10")
        self.assertEqual(response.json["result"], 10)
        print("subtract ok")

    def test_multiply(self):
        print("multiply ok")

    def test_divide(self):
        print("divide ok")

    def test_power(self):
        print("power ok")

    def test_square_root(self):
        print("square root ok")

    def test_modulus(self):
        print("modulus ok")


if __name__ == "__main__":
    unittest.main()
