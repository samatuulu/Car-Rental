from django.urls import path

from accounts.views import login_view, logout_view, register_view, UserDetailView, UserUpdateView, \
    UserUpdatePasswordView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', register_view, name='registration'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('profile/update_password/<int:pk>/', UserUpdatePasswordView.as_view(), name='user_change_password')
]

app_name = 'accounts'
