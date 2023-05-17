from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers
from Wallapop import views

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
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
