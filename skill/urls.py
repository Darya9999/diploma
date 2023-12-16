"""skill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from statistic.views import showAnkets
from statistic.views import post_new
from statistic.views import show_ankets
from statistic.views import delete_elem
from statistic.views import update_elem
from statistic.views import delete_all
from statistic.views import graph

urlpatterns = [
    path('admin/', admin.site.urls),
    path('statistic/', post_new ),
    path('ankets/', show_ankets ),
    path('ankets/delete/', delete_elem ),
	path('ankets/update/', update_elem ),
	path('ankets/deleteall/', delete_all ),
	path('stat/', graph ),
]
