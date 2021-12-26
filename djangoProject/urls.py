"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog_t/', include('blog_t.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    # path('', main_page),
    # path('<int:year>/<int:month>/<int:day>/<str:slug>', detail_view),
    path('blog/', include(('blog.url', 'blog'), namespace='blog')),
    path('form/', include(('form.urls', 'form'), namespace='form')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# line 29 / 30
