from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),

    path('', include('app.base.urls')),
    path('contracts/', include('app.contracts.urls')),    
    path('requisitions/', include('app.requisitions.urls')),    
    path('dispatches/', include('app.dispatches.urls')),    
]
