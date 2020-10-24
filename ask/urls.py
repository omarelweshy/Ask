from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin', admin.site.urls),

    # Apps
    path('', include('pages.urls')),
    path('', include('users.urls')),
    path('notifications/', include('notifications.urls')),

    # ALLAUTH
    path('account/', include('allauth.urls')),
    path('account/password/reset/', auth_views.PasswordResetView.as_view(
        html_email_template_name='account/password_reset_html_email.html'
    )),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
