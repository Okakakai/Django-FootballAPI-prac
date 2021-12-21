from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# /player/でviewにアクセスできるようにする
router.register(r'players', views.PlayerViewSet)
# なんかルータだとできないからurlpatternsで記述
# router.register(r'position', views.PlayerPositionListView)
# router.register(r'age', views.KariViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('position/', views.PlayerPositionListView.as_view())
]
