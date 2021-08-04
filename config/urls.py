"""config URL Configuration

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
from django.urls import path, include

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),  # after use django-allauth

    # Local apps
    path('', include('pages.urls')),
    path('books/', include('books.urls')),  # new

    # after use django-allauth, we can delete the URL path for our accounts app,
    # and we can delete accounts/urls.py and accounts/views.py
    # path('accounts/', include('accounts.urls')),

]
