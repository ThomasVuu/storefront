from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from pprint import pprint

router = DefaultRouter()
router.register('products', views.ProdctViewSet)
router.register('collections', views.CollectionViewSet, basename='collection')

# URLConf
urlpatterns = router.urls
