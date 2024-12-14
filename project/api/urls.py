# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkflowViewSet, create_model, FitModelAPIView, PredictAPIView, ScalerAPIView, FitScalerAPIView
from .views import TransformAPIView, FitTransformAPIView, TrainTestSplitAPIView
router = DefaultRouter()
router.register(r'workflows', WorkflowViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('create_model/', create_model, name='create_model'),
    path('fit_model/', FitModelAPIView.as_view(), name='fit_model'),
    path('predict/', PredictAPIView.as_view(), name='predict_model'),
    path('create_scaler/', ScalerAPIView.as_view(), name='create_scaler'),
    path('fit_scaler/', FitScalerAPIView.as_view(), name='fit_scaler'),
    path('transform/', TransformAPIView.as_view(), name='transform'),
    path('fit_transform/', FitTransformAPIView.as_view(), name='fit_transform'),
    path('train_test_split/', TrainTestSplitAPIView.as_view(), name='train_test_split'),
]
