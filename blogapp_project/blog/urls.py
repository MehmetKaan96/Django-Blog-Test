from django.urls import path
from . import views

#https://127.0.0.1:800/        => index
#https://127.0.0.1:800/index   => index
#https://127.0.0.1:800/blogs   => blogs
#https://127.0.0.1:800/blogs/3 => blog-details


urlpatterns = [
    path("",views.index),
    path("index",views.index),#=> https://127.0.0.1:800/index
    path("blogs",views.blogs),
    path("blogs/<int:id>",views.blogs_details),
]