from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='notes API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('note.urls')),
    path('auth/', include('rest_framework.urls')),
    
    path('api/jwtauth/', include('jwtauth.urls'), name='jwtauth'),
    path('api/docs', schema_view)
]
