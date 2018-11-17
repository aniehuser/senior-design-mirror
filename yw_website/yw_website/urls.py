"""yw_website URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from website import views as yw_website_views
# from yw_rest_services import views as yw_rest_services_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', yw_website_views.home, name='home'),
    path('upload/', yw_website_views.model_form_upload, name='upload'),
    # path('save/ping', yw_rest_services_views.yw_save_ping, name='ping'),
    path('home/', yw_website_views.DocumentListView.as_view(), name='home'),
    path('home/detailed_workflow/', yw_website_views.detailed_workflow, name = 'detailed_workflow'),
    path('home/run_detail/', yw_website_views.run_detail, name='run_detail'),
    # path('home/', views.home, name='home'),
    path('home/', include('django.contrib.auth.urls'), name ='login'),
    path('home/register/', yw_website_views.register, name='register'),
    path('home/users/', yw_website_views.users, name = 'users'),
    path('upload/', yw_website_views.model_form_upload, name='upload'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
