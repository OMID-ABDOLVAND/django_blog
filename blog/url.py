from django.urls import path
from blog.views import BlogDetailView, BlogListView, SharePost

urlpatterns = [
    # path('', main_page),
    path('', BlogListView.as_view()),
    path('<int:year>/<int:month>/<int:day>/<str:slug>', BlogDetailView.as_view(), name='blog-item'),
    path('share/<int:pk>', SharePost.as_view(), name='share-post'),
    ]
