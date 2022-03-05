from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# /player/でviewにアクセスできるようにする
router.register(r'players', views.PlayerViewSet)
# なんかルータだとできないからurlpatternsで記述
# router.register(r'position', views.PlayerPositionListView)
# router.register(r'age', views.KariViewSet)
router.register(r'headcoachers', views.HeadCoachViewSet)

router.register(r'player-type', views.PlayerTypeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('player-position/', views.PlayerPositionListView.as_view())
]
