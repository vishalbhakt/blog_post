from django.urls import path
from . import views
from . views import register, user_login, user_logout
urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('home',views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/new/', views.post_new, name='post_new'),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    # path('users/', views.user_list, name='user_list'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
]