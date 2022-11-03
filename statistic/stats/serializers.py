from rest_framework.serializers import ModelSerializer

from stats.models import BgStat, AdStat


class BgStatSerializer(ModelSerializer):
    class Meta:
        model = BgStat
        fields = '__all__'


class AdStatSerializer(ModelSerializer):
    class Meta:
        model = AdStat
        fields = '__all__'
