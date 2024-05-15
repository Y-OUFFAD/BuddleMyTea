

from django.contrib import admin
from django.urls import include, path
from testamoi.views import Index, Registration, Login, Order, Product, Shop, createAndReadCookies
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path("Admin/", admin.site.urls),
    path('', views.Login, name='Login'),
    path('register/', views.Registration, name="Register"),
    path('Order/', views.Order, name='Order'),
    path('Product/',views. Product, name='Product'),
    path('Shop/',views. Shop, name='Shop'),
    path('singnup/',views. singnup, name='singnup'),
    path('Login/',views. Login, name='Login'),
    path('createAndReadCookies/',views.createAndReadCookies, name='createAndReadCookies'),
]

# urlpatterns = [

#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
#     path('', include('myapp.urls')), # include your app urls.py here
# ]
