import django
from django.urls import include, path
from blog.views import BlogDetailView, BlogListView, SharePost
# from django.contrib.auth.urls
urlpatterns = [
    # path('', main_page),
    path('', BlogListView.as_view()),
    path('<int:year>/<int:month>/<int:day>/<str:slug>', BlogDetailView.as_view(), name='blog-item'),
    path('share/<int:pk>', SharePost.as_view(), name='share-post'),
    
    ]
