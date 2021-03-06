from rest_framework import routers
from .views import *
from django.conf.urls import url, include

router = routers.SimpleRouter()
router.register(r'resources', ResourceList)
router.register(r'votings', VotingViewSet)

urlpatterns = [url(r'^', include(router.urls))]
