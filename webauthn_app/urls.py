# urls.py for webauthn_app
from django.urls import path, include
from .views import manage, user_verification

app_name = "webauthn_app"


urlpatterns = [
    # Illegal request handling
    path('reject/', user_verification.illegal_request, name='illegal_request'),

    # user authentication
    path('login/', user_verification.user_login, name='login'),
    path('register/', user_verification.register, name='register'),
    path('logout/', user_verification.logout, name='logout'),

    # Account management views
    path('', manage.manage_account, name='manage_account'),
    path('password/', manage.change_password, name='manage_password'),
]
