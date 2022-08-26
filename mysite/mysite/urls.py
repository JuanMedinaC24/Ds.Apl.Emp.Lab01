from django.contrib import admin
from django.urls import include, path
 
urlpatterns = [
    path('polls/', include('encuesta.urls')),
    path('app/',include('app.urls')),
    path('admin/', admin.site.urls),
]
