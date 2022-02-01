from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]

# client id
#556130642953-3th50pc7sm6dqu0hmbghgr9eb2lpsnpp.apps.googleusercontent.com

# client secret
#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