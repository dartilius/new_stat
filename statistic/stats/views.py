from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from stats.models import BgStat, AdStat
from stats.serializers import BgStatSerializer, AdStatSerializer


class BgViewSet(ModelViewSet):
    queryset = BgStat.objects.all()
    serializer_class = BgStatSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        if 'data' in kwargs:
            data = kwargs['data']

            if isinstance(data, list):
                kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)


class AdViewSet(ModelViewSet):
    queryset = AdStat.objects.all()
    serializer_class = AdStatSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        if 'data' in kwargs:
            data = kwargs['data']

            if isinstance(data, list):
                kwargs['many'] = True

        return super().get_serializer(*args, **kwargs)