from django.urls import path
from blog import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('post_detail/<int:pk>/', views.post_detail, name="post_detail"),
    path('create_post/', views.create_post, name='create_post'),
    path('my_posts/', views.my_posts, name='my_posts'),
    path('update_post/<int:pk>/', views.update_post, name='update_post'),
    path('delete_post/<int:pk>/', views.delete_post, name="delete_post"),
    path('404/', views.page_404, name="page_404"),
    path('logout/', views.logout_view, name='logout'),
]
