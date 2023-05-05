from rest_framework.serializers import ModelSerializer

from stats.models import BgStat, AdStat, TwoDaysBgStat, TwoDaysAdStat


class BgStatSerializer(ModelSerializer):
    class Meta:
        model = BgStat
        fields = '__all__'

    def create(self, validated_data):
        model_two = TwoDaysBgStat.objects.create(**validated_data)
        return BgStat.objects.create(**validated_data)


class AdStatSerializer(ModelSerializer):
    class Meta:
        model = AdStat
        fields = '__all__'

    def create(self, validated_data):
        model_two = TwoDaysAdStat.objects.create(**validated_data)
        return AdStat.objects.create(**validated_data)
