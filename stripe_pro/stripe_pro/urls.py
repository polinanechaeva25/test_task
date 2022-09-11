from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from mainapp.views import ItemList, ItemDetailView, BuyItemView, StartView

router = DefaultRouter()
router.register('buy', BuyItemView)

urlpatterns = [
    path('item/', ItemList.as_view(), name='index'),
    path('', StartView.as_view(), name='start'),
    path('item/<int:pk>', ItemDetailView.as_view(), name='item'),

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
