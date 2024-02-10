from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_posts, name='list_posts'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('/page/<int:page_number>', views.paginate_posts, name='paginate_posts'),
]
