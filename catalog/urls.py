from django.urls import path

from catalog.apps import ProductConfig

app_name = ProductConfig.name

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('catalog.urls', namespace='catalog'))
]
