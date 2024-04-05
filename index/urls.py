from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_page, name='login'),
    path('sign_up/', sign_up, name='sign_up'),
    path('logout/', logout_user, name='logout'),
    path('post_create/', post_create, name='post_create'),
    path('user_posts/', user_posts, name='user_posts'),
    path('post_details/<int:pk>/', post_details, name='post_details'),
    path('post_udate/<int:pk>/', post_update, name='post_update'),
    path('post_delete/<int:pk>/', post_delete, name='post_delete'),
    path('pricing/', pricing_page, name='pricing'),
    path('features/', features_page, name='features'),
    path('faqs/', faqs_page, name='faqs'),
]