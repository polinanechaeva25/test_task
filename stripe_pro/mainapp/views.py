from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
# from requests import Response
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Item
from .serialazers import ItemModelSerializer

import stripe


class TitleContextMixin:

    def get_title(self):
        return getattr(self, 'title', '')

    def get_context_data(self, **kwargs):
        context = super(TitleContextMixin, self).get_context_data(**kwargs)
        context.update(
            title=self.get_title()
        )
        return context


class StartView(TitleContextMixin, ListView):
    model = Item
    title = 'Start'
    template_name = 'mainapp/start.html'


class ItemList( TitleContextMixin, ListView):
    model = Item
    title = 'Items'
    template_name = 'mainapp/index.html'

    def get_queryset(self):
        res = Item.objects.all()
        return res


class ItemDetailView(TitleContextMixin, DetailView):
    model = Item
    title = 'Item'
    template_name = 'mainapp/item.html'


class BuyItemView(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemModelSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'

        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': instance,
                        'description': instance.description,
                    },
                    'unit_amount': int(float(instance.price) * 100),

                },
                'quantity': 1,

            }],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )

        return Response(session)



