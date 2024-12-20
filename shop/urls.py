from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name = 'home'),
    path('register/', register, name = 'register'),
    path('login/', login_page, name = 'login'),
    path('logout/', logout_page, name = 'logout'),
    path('collections/', collections, name = 'collections'),
    path('collections/<str:name>', collectionsview, name = 'collections'),
    path('collections/<str:cname>/<str:pname>', product_details, name = 'product_details'),
]