"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.views import static as stat
from appprofile import views as profileviews
from donation import views as donationviews

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)$', stat.serve, {'document_root': settings.STATIC_ROOT}),
    path('learnmore',profileviews.learnmore),
    path('store',profileviews.store),
    path('donate',profileviews.donate),
    path('donate/now',donationviews.donatenow),
    path('donate/do',donationviews.donate),
    path('auth',profileviews.auth),
    path('',profileviews.homepage),
]

admin.site.site_header = "RobinHood Admin Panel"