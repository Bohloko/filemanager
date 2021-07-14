from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ApplicationFileViewSet, FileUploadViewSet, UserViewSet, FileSearchView

router = SimpleRouter()
router.register('users', UserViewSet, basename = 'users' )
router.register('files', ApplicationFileViewSet, basename = 'files')
router.register('upload', FileUploadViewSet, basename = 'uploads')

urlpatterns = router.urls
urlpatterns.append(
    path('search/', FileSearchView.as_view(), name='search'),
)
urlpatterns.append(
    path('api-auth', include('rest_framework.urls'))
)
urlpatterns.append(
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
)
urlpatterns.append(
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
)

