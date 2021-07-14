from django.urls import path
from . import views


urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('blog/<slug>/', views.blog, name='blog'),
    # path('view/<id>/', views.view, name='view'),
    # path('view-all/', views.view-all, name='view-all'),
    path('edit_post/<id>/', views.edit_post, name='edit_post'),
    path('delete_post/<id>/', views.delete_post, name='delete_post'),
    path('create_post/', views.create_post, name='create_post'),
    # path('create/', views.PostCreate.as_view(), name='post-create'),
    path('update/<int:pk>/', views.PostUpdate.as_view(), name='post-update'),
    path('delete/<int:pk>/', views.PostDelete.as_view(), name='post-delete'),
]