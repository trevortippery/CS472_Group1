"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""

from unittest import TestCase

# we need to import the unit under test - counter
from src.counter import app

# we need to import the file that contains the status codes
from src import status


class CounterTest(TestCase):
    """Counter tests"""

    def setUp(self):
        self.client = app.test_client()

    def test_create_a_counter(self):
        """It should create a counter"""
        client = app.test_client()
        result = client.post('/counters/foo')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    def test_duplicate_a_counter(self):
        """It should return an error for duplicates"""
        client = app.test_client()
        result = client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = client.post('/counters/bar')
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)

    def test_update_a_counter(self):
        """It should update the counter"""
        client = app.test_client()
        result = client.post('/counters/col')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        baseline_value = result.get_json()['col']
        self.assertEqual(baseline_value, 0)
        update_result = client.put('/counters/col')
        self.assertEqual(update_result.status_code, status.HTTP_200_OK)
        update_result_value = update_result.get_json()['col']
        self.assertEqual(update_result_value, baseline_value + 1)

    def test_read_a_counter(self):
        """It should read the counter"""
        client = app.test_client()
        result = client.post('/counters/loo')
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        read_result = client.get('/counters/loo')
        self.assertEqual(read_result.status_code, status.HTTP_200_OK)
        fake_result = client.get('/counters/fake')
        self.assertEqual(fake_result.status_code, status.HTTP_404_NOT_FOUND)
