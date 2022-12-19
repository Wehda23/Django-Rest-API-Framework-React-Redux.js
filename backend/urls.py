from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='build/index.html')),
    path('api/products/',include('base.urls.product_urls')),
    path('api/users/',include('base.urls.users_urls')),
    path('api/orders/',include('base.urls.orders_urls')),

]


urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)