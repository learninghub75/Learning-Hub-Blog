from django.urls import path
from .views import PostList

app = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='home'),
]
