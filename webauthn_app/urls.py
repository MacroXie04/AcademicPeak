# urls.py for webauthn_app
from django.urls import path
from .views import user_verification

app_name = "webauthn_app"

urlpatterns = [
    # user authentication
    path('login/', user_verification.user_login, name='login'),
    path('register/', user_verification.register, name='register'),
    path('logout/', user_verification.logout, name='logout'),
]
