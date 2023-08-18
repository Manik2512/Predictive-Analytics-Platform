# code
from django.contrib import admin
from django.urls import path
from . import views
from . import views1

urlpatterns = [
	path('admin/', admin.site.urls),
	path("", views.index),
	path("predict/", views.predict),
	path("predict/result", views.result),
    path("about",views.about, name="about"),
    path("contact",views.contact, name="contact"),
    path("predict1/", views1.predict1),
    path("predict1/result1", views1.result1)
    
]