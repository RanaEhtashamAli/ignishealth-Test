from django.db.models import Sum, F
from rest_framework import viewsets
from rest_framework.fields import FloatField
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Data
from .serializers import DataSerializer, AggImpClkSerializer, AggInstallSerializer, AggRevenueSerializer, \
    AggCpiSpndSerializer
from .pagination import DataResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

# Create your views here.


class DataView(viewsets.ReadOnlyModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    pagination_class = DataResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {'date': ['gte', 'lte', 'gt', 'lt', 'exact'], 'channel': ['exact'], 'country': ['exact'],
                        'os': ['exact']}
    ordering_fields = ['date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue']

    @action(detail=False, methods=['get'])
    def AggImpClkView(self, request):
        queryset = self.filter_queryset(self.get_queryset().values('channel', 'country')
                                        .annotate(impressions=Sum('impressions'), clicks=Sum('clicks')))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = AggImpClkSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AggImpClkSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def AggInstallView(self, request):
        queryset = self.filter_queryset(self.get_queryset().values('date')
                                        .annotate(installs=Sum('installs')))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = AggInstallSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AggInstallSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def AggRevenueView(self, request):
        queryset = self.filter_queryset(self.get_queryset().values('os')
                                        .annotate(revenue=Sum('revenue')))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = AggRevenueSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AggRevenueSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def AggCpiSpndView(self, request):
        queryset = self.filter_queryset(self.get_queryset().values('channel').annotate(spend=Sum('spend'))
                                        .annotate(install_sum=Sum('installs'))
                                        .annotate(cpi=F('spend') / F('install_sum'))).order_by('-cpi')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = AggCpiSpndSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AggCpiSpndSerializer(queryset, many=True)
        return Response(serializer.data)
