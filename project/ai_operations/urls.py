# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import create_model , FitModelAPIView, PredictAPIView, PreprocessorAPIView, FitPreprocessorAPIView
from .views import TransformAPIView, FitTransformAPIView, TrainTestSplitAPIView
router = DefaultRouter()
# router.register(r'workflows', WorkflowViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    # Model
    path('create_model/', create_model, name='create_model'),
    path('fit_model/', FitModelAPIView.as_view(), name='fit_model'),
    path('predict/', PredictAPIView.as_view(), name='predict_model'),

    # preprocessor
    path('create_preprocessor/', PreprocessorAPIView.as_view(), name='create_preprocessor'),
    path('fit_preprocessor/', FitPreprocessorAPIView.as_view(), name='fit_preprocessor'),
    path('transform/', TransformAPIView.as_view(), name='transform'),
    path('fit_transform/', FitTransformAPIView.as_view(), name='fit_transform'),

    # train_test_split
    path('train_test_split/', TrainTestSplitAPIView.as_view(), name='train_test_split'),
]