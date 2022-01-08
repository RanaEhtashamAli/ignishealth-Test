from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    cpi = serializers.SerializerMethodField()
    class Meta:
        model = Data
        exclude = ['id', 'created_at', 'updated_at', 'is_deleted', 'is_active']

    def get_cpi(self, obj):
        return obj.spend/obj.installs


class AggImpClkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['channel', 'country', 'impressions', 'clicks']


class AggInstallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['date', 'installs']


class AggRevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['os', 'revenue']

class AggCpiSpndSerializer(serializers.ModelSerializer):
    cpi = serializers.FloatField()
    class Meta:
        model = Data
        fields = ['cpi', 'spend', 'channel']
