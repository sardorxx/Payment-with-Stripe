from django.urls import path
from .views import BuyItemView, ItemDetailView, SomeDefaultView

app_name = 'payment'

urlpatterns = [
    path('', SomeDefaultView.as_view(), name='default_view'),
    path('buy/<int:id>/', BuyItemView.as_view(), name='buy_item'),
    path('item/<int:id>/', ItemDetailView.as_view(), name='item_detail'),
]
