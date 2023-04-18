from django.urls import path

from users.views.reset_password import GetResetLinkView, ResetPasswordView
from users.views.sign_in import SignInView
from users.views.sign_in_social import GoogleLogin, FacebookLogin
from users.views.sign_out import SignOutView
from users.views.sign_up import SignUpView, ConfirmView, ResendConfirmationEmailView
from users.views.users import UsersListView, UserSettingsView, UserAvatarSettingsView, ChangePasswordView, \
    UsersSearchView
from users.views.users import UserDetailView

urlpatterns = [
    path('sign-in', SignInView.as_view(), name='signin'),
    path('sign-in/google', GoogleLogin.as_view(), name='signin-google'),
    path('sign-in/facebook', FacebookLogin.as_view(), name='signin-facebook'),
    path('sign-up', SignUpView.as_view(), name='signup'),
    path('sign-out', SignOutView.as_view(), name='signout'),
    path('confirm', ConfirmView.as_view(), name='confirm'),
    path('user', UsersListView.as_view(), name='user-list'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user-detail'),
    path('user/<str:search>', UsersSearchView.as_view(), name='user-search'),
    path('user_settings', UserSettingsView.as_view(), name='user-settings'),
    path('user_change_avatar', UserAvatarSettingsView.as_view(), name='user-change-avatar'),
    path('change_password', ChangePasswordView.as_view(), name='change-password'),
    path('reset_link', GetResetLinkView.as_view(), name='reset-link'),
    path('reset_password', ResetPasswordView.as_view(), name='reset-password'),
    path('resend_confirmation/<int:pk>', ResendConfirmationEmailView.as_view(), name='resend-confirmation'),
]
