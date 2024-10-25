from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
import json

class TrainTestSplitViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('train_test_split')  # Make sure this matches the name in your urls.py

    def test_train_test_split(self):
        data = {
            'data': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
            'test_size': 0.3,
            'random_state': 42
        }
        response = self.client.post(self.url, data=json.dumps(data), content_type='application/json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        result = response.json()
        print("\n--- Train-Test Split Results ---")
        print(f"Training set: {result['X_train']}")
        print(f"Test set: {result['X_test']}")
        print("--------------------------------")
        self.assertIn('X_train', result)
        self.assertIn('X_test', result)
        
        # Check if the split is correct
        self.assertEqual(len(result['X_train']), 7)  # 70% of 10
        self.assertEqual(len(result['X_test']), 3)   # 30% of 10
        
        # Check if all original data is present in the split
        all_data = result['X_train'] + result['X_test']
        self.assertEqual(sorted(all_data), [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])

    def test_invalid_input(self):
        data = {
            'data': 'not a list',
            'test_size': 0.3
        }
        response = self.client.post(self.url, data=json.dumps(data), content_type='application/json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)