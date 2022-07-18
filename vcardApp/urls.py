from django.urls import path

from .views import (CategoryAPIView,
                            CouponListAPIView,
                            GalleryAPIView,
                            OrderAddAPIView,
                            OrderListAPIView,
                            OrderUpdateAPIView,
                            ProductDetailAPIView,
                            ProductAPIView)

urlpatterns = [
    path('', CategoryAPIView.as_view(), name='categories'),
    path('products/', ProductAPIView.as_view(), name='products'),
    path('products/<prod_id>/', ProductDetailAPIView.as_view(), name='products'),
    path('orders/add/', OrderAddAPIView.as_view(), name='orders-add'),
    path('orders/list/', OrderListAPIView.as_view(), name='orders-list'),
    path('orders/list/<ord_id>/', OrderUpdateAPIView.as_view(), name='orders-update'),
    path('coupon/', CouponListAPIView.as_view(), name='coupons'),
    path('gallery/', GalleryAPIView.as_view(), name='gallery'),
]
