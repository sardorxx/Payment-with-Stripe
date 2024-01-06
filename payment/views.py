import stripe
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import Item

stripe.api_key = 'sk_test_51OVAfYCUflyCYNASwdLrPMrtDmGkNoZE15wBHvXndyVY4E1Dspf6KiZk9DDZByhPE1QJZwRxuHpAl6ejw0LRlLlt0007lheE2a'


class BuyItemView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )
        return redirect(session.url)
        # return JsonResponse({'session_id': session.id})


class ItemDetailView(View):
    def get(self, request, id):
        item = get_object_or_404(Item, id=id)
        return render(request, 'item_detail.html', {'item': item})


class SomeDefaultView(View):
    def ok(self, request):
        return render(request, 'ok.html')
