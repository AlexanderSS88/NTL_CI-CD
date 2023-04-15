from django.test import TestCase, Client


class TestMyApp(TestCase):

    def test_my_stocks(self):
        client = Client()
        response = client.get('/stocks/')
        self.assertEqual(response.status_code, 200)

    def test_my_products(self):
        client = Client()
        response = client.get('/products/')
        self.assertEqual(response.status_code, 200)
