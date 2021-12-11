from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# /player/でviewにアクセスできるようにする
router.register('players',views.PlayerViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('/', include(router.urls))
]
