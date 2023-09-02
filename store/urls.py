from django.urls import path
from rest_framework_nested import routers
from . import views
from pprint import pprint

router = routers.DefaultRouter()
router.register('products', views.ProdctViewSet, basename='products')
router.register('collections', views.CollectionViewSet, basename='collection')
router.register('carts', views.CartViewSet, basename='carts')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

# URLConf
urlpatterns = router.urls + products_router.urls
