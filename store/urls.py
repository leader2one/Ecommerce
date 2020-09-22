from django.urls import path

from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('update_item/', views.updateItem, name='update_item'),
	path('process_order/', views.processOrder, name='process_order'),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.png')))
]