from django.test import TestCase, Client


class TestMyApp(TestCase):

    def test_my_stocks(self):
        client = Client()
        response = client.get('http://127.0.0.1:8000/api/v1/stocks/')
        self.assertEqual(response.status_code, 200)

    def test_my_products(self):
        client = Client()
        response = client.get('http://127.0.0.1:8000/api/v1/products/')
        self.assertEqual(response.status_code, 200)
