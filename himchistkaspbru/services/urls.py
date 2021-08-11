from django.urls import path, re_path
from django.views.decorators.cache import cache_page
from .views import *
urlpatterns = [
    path('', cache_page(60)(Service_Home.as_view()), name='home'),
    path('about/', about, name='about'),
    path('questions_and_answers/', Service_Questions_And_Answers.as_view(), name='questions_and_answers'),
    path('contact/', contact, name='contact'),
    path('review/', Service_Review.as_view(), name='review'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('addorder/', addorder, name='add_order'),
    path('gretorder/', greatorder, name='great_order'),
    path('addclient/', addclient, name='addclient'),


]