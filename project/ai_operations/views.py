from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sklearn.model_selection import train_test_split

import numpy as np

# Create your views here.


@api_view(['POST'])
def train_test_split_view(request):
    data = request.data.get('data', [])
    test_size = request.data.get('test_size', 0.2)
    random_state = request.data.get('random_state', None)

    try:
        # Convert data to numpy array
        X = np.array(data)
        
        # Perform train-test split
        X_train, X_test = train_test_split(X, test_size=test_size, random_state=random_state)
        
        # Convert numpy arrays back to lists for JSON serialization
        return Response({
            'X_train': X_train.tolist(),
            'X_test': X_test.tolist()
        })
    except Exception as e:
        return Response({'error': str(e)},status=400)