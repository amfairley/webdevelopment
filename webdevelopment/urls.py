"""
URL configuration for webdevelopment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('intro_to_full_stack/', include('intro_to_full_stack.urls')),
    path('HTML/', include('HTML.urls')),
    path('CSS/', include('CSS.urls')),
    path('JavaScript/', include('javascript_app.urls')),
    path('Python/', include('python_app.urls')),
    path('Backend/', include('backend.urls')),
    path('Flask/', include('flask_app.urls')),
    path('Analytics/', include('analytics.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
