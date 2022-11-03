from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from stats.models import BgStat, AdStat
from stats.serializers import BgStatSerializer, AdStatSerializer


class BgViewSet(ModelViewSet):
    queryset = BgStat.objects.all()
    serializer_class = BgStatSerializer
    permission_classes = [IsAuthenticated]


class AdViewSet(ModelViewSet):
    queryset = AdStat.objects.all()
    serializer_class = AdStatSerializer
    permission_classes = [IsAuthenticated]
