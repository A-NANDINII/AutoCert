import unittest
import os
import tempfile
from app import app

class AutoCertTestCase(unittest.TestCase):
    def setUp(self):
        # Configure test client
        app.config['TESTING'] = True
        app.config['UPLOAD_FOLDER'] = tempfile.mkdtemp()
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'AutoCert', response.data)

    def test_file_upload(self):
        # Create test files
        with open('test.csv', 'w') as f:
            f.write("Name,Event\nTest User,Test Event")
        
        # Test upload
        with open('test.csv', 'rb') as csv:
            response = self.client.post(
                '/generate',
                data={
                    'template': (open('test.jpg', 'rb'), 'test.jpg'),
                    'csv': csv
                },
                content_type='multipart/form-data'
            )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/pdf')

if __name__ == '__main__':
    unittest.main()