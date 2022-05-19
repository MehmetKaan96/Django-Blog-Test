"""blogapp URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#https://127.0.0.1:800/        => index
#https://127.0.0.1:800/index   => index
#https://127.0.0.1:800/blogs   => blogs
#https://127.0.0.1:800/blogs/3 => blog-details

"""
path('user/',include('blog.urls')) dersek yukarıdaki URL'ler 
şöyle değiştirilmeli:

https://127.0.0.1:800/user        => index
https://127.0.0.1:800/user/index   => index
https://127.0.0.1:800/user/blogs   => blogs
https://127.0.0.1:800/user/blogs/3 => blog-details
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    # path('user/',include('blog.urls'))
]
