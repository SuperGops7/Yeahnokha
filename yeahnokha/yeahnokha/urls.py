"""yeahnokha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from events.views import events_view
from register.views import register_success_view,register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', name = "home"),
    path('events/', events_view, name = "Events"),
    path('register/', register_view, name = "Register"),
    path('register_success/', register_success_view, name = "Register"),
]
