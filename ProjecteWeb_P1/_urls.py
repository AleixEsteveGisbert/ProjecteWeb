"""ProjecteWeb_P1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Wallapop import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.ads_list_view, name='home'),
    path('admin/', admin.site.urls),
    path('login/', views.login_form, name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('register', views.register_form, name='register'),
    path('ad/<int:ad_id>', views.get_ad, name='ad-show'),
    path('ad/<int:ad_id>/edit', views.ad_edit, name='ad-edit'),
    path('ad/<int:ad_id>/delete', views.ad_delete, name='ad-delete'),
    path('ad/new', views.ad_new, name='ad-new'),
    path('comment/<int:comment_id>/edit', views.comment_edit, name='comment-edit'),
    path('comment/<int:comment_id>/delete', views.comment_delete, name='comment-delete'),
    path('user/edit', views.edit_profile, name='profile-edit'),
    path('user/<int:user_id>', views.get_profile, name='profile'),
    path('user/ads', views.get_userAds, name='user-ads'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
