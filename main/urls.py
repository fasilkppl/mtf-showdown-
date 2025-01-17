"""
URL configuration for techfest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from userreg import views as user_views
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import handler404
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.contact_email, name='landing_pg'),
    path('home/', user_views.contact_email, name='landing_pg'),
    path('home', user_views.contact_email, name='landing_pg'),
    path('home/pt', user_views.contact_email2, name='project_treasury'),
    path('home/pt/', user_views.contact_email2, name='project_treasury'),
    
]




def custom_404(request, exception):
    return render(request, 'userreg/404.html', status=404)
handler404 = custom_404



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


