import unittest
from app import app  # Import the Flask app instance from your app.py

class TestApp(unittest.TestCase):  # Ensure the class name matches the test file name
    def setUp(self):
        # Set up the Flask test client
        self.client = app.test_client()

    def test_test_route(self):
        # Send a GET request to the /api/test route
        response = self.client.get('/api/test')  # Ensure the URL matches your app's setup
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Test was successful.')

if __name__ == '__main__':
    unittest.main()