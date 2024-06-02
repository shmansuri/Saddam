
from django.contrib import admin
from django.conf import settings
from django.conf.urls import static
from django.urls import path, include
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='Home'),
    path('contactus/', views.contact , name='contact'),
    path('project/', include('project.urls')),
    path('skill', include('skill.urls')),
]
