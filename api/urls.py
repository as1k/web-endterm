from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from api.views.fbv import create_user, PostViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"", PostViewSet, "log")

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('signup/', create_user),
    path('post/', include(router.urls)),
]