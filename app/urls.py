from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('app.base.urls')),
    path('contracts/', include('app.contracts.urls')),    
    path('requisitions/', include('app.contracts.urls')),    
]
