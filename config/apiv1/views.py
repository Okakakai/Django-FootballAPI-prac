from rest_framework.response import Response
from rest_framework import viewsets, generics, filters
from players.models import Player
from .serializers import PlayerSerializer, PositionSerializer


class PlayerViewSet(viewsets.ModelViewSet):

    queryset = Player.objects.all().order_by('playername', 'date')
    serializer_class = PlayerSerializer
    filter_fields = ('playername', 'nationality')
class PlayerPositionListView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PositionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['playername', 'suitableposition_type']







# pretty my memories
# class PositionViewSet(views.APIView):
#     queryset = Player.objects.all()
#     serializer_class = PositionSerializer
#     filter_fields = ('mostsuitableposition_type',)
#     # def get(self, request, p=None):
#     #     data = Player.objects.filter(suitableposition_type__contains=p)
#     #     serializer = PositionSerializer(data=data, many=True)
#     #     serializer.is_valid()

#     #     return Response(serializer.validated_data)
#     def get(self, request, p):
#         data = Player.objects.filter(
#             mostsuitableposition_type__contains=p)
#         serializer = PositionSerializer(data=data, many=True)
#         serializer.is_valid()
#         return Response(data)

# class PlayerPositionViewSet(generics.ListCreateAPIView):
#     serializer_class = PositionSerializer

#     def get_queryset(self):
#         queryset = Player.objects.all()
#         position = self.request.query_params.get('suitableposition_type', None)
#         if position is not None:
#             queryset = queryset.filter(
#                 purchaser__=position)  # 「__icontains」を追加する
#         return queryset

