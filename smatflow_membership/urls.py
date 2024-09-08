from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.views.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('users.urls')),
    # Add other URL patterns here
)