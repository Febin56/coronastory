from django.urls import path
from .views import HomeView, PostView, CreatePostView, like_post
from blog import views



urlpatterns = [
    path('', HomeView.as_view(), name = 'bloghome'),
    path('post/<int:pk>/', PostView.as_view(), name = 'blogdetail'),
    path('create_post/', CreatePostView.as_view(success_url='/'), name = 'createpost'),
    path('like/', views.like_post, name="like_post"),
    
]