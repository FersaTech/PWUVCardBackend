from django.urls import path

from vcardApp.views import CategoryAPIView, ProductAPIView

urlpatterns = [
    path('', CategoryAPIView.as_view(), name='categories'),
    path('products/', ProductAPIView.as_view(), name='products'),
]
