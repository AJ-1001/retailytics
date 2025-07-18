from django.urls import path
from .views import main_page, sales_add, sales_top, sales_list

urlpatterns = [
    path('', main_page, name='main_page'),
    path('add-sale/', sales_add, name="add_sale"),
    path('top-sales/', sales_top, name="sales_top"),
    path('sales-html/', sales_list, name="sales_html"),
]
