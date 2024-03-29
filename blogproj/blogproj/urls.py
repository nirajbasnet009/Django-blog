
from django.contrib import admin
from django.urls import path,include
from users import views as users_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('blog.urls')),

    # User authentication
    path('register/',users_views.register,name='register'),
    path('profile/',users_views.profile,name='profile'),
    path('profile/profile_update',users_views.profile_update,name='profile_update'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='Login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='Logout')

]
if settings.DEBUG: 
  urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

