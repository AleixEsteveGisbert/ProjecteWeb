from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from Wallapop import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'ads', views.AdViewSet)
router.register(r'comments', views.CommentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('user/<int:user_id>', views.get_profile, name='profile'),
    path('ad/<int:ad_id>', views.get_ad, name='ad'),
    path('ad/<int:ad_id>/edit', views.ad_edit, name='ad-edit'),
    path('ads/new', views.ad_new, name='ad-new'),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('api/retrieve-user', views.retrieve_user, name="retrieve-user"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
