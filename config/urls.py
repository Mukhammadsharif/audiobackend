from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include([
        path('main/', include(('main.urls', 'main'), namespace='main')),
        path('users/', include(('users.urls', 'users'), namespace='users')),
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
