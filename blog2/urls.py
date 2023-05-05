

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',views.home_view, name='home'),
    path ('my_cv/',include ('moncv.urls'),name='my_cv'),
    path ('projects/',include ('mesprojets.urls'),name='projects'),
]
