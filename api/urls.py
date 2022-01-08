from django.urls import path
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'data', DataView)

urlpatterns = [
]

urlpatterns += router.urls