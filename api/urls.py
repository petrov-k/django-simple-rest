from django.urls import path
from . import views

urlpatterns = [
    path('blogpost/', views.BlogPostListCreate.as_view(), name='blogpost_view_create'),
    path('blogpost/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='blogpost_view_retrieve_update_destroy'),
    path('blogpost-list/', views.BlogPostList.as_view(), name='blogpost_view_list'),
]
