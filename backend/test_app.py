import unittest
from flask import Flask
from app import app

class TestAPIRoutes(unittest.TestCase):
    def setup(self):
        # Set up the test client
        self.client = app.test_client()
        self.client.testing = True

    def test_test_route(self):
        # Simulate a GET request to the /test endpoint
        response = self.client.get('/api/test')  # Ensure the URL matches your route setup
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Test was successful.')

if __name__ == '__main__':
    unittest.main()