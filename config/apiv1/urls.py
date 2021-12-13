from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# /player/でviewにアクセスできるようにする
router.register(r'players',views.PlayerViewSet)


urlpatterns = [
    path('', include(router.urls))
]
