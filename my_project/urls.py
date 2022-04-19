from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cart/', include('cart.urls')),
    path('shop/', include('shop.urls')),
    path('about/', include('about.urls')),
    path('offers/', include('offers.urls')),
    path('contact/', include('contact.urls')),
    path('search/', include('search.urls')),
    path('orders/', include('orders.urls')),


    path('', TemplateView.as_view(template_name='home.html'), name='home')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)