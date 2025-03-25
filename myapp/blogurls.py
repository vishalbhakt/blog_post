from django.urls import path
from . import views
from . views import register, user_login, user_logout
# from myapp.views import post_view, user_login
urlpatterns = [
    # path('post/', post_view, name='post'), 
    path('',views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
]