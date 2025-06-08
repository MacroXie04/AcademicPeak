from django.urls import path, include

# API URL patterns with versioning
urlpatterns = [
    # API v1
    path('v1/ranking/', include('ranking.api.urls')),
    path('v1/webauthn/', include('webauthn_app.api.urls')),
    path('v1/theia/', include('theia_ide.api.urls')),
    path('v1/index/', include('index.api.urls')),
]
