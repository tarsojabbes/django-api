from django.urls import path

from . import views

urlpatterns = [
    path("posts/", views.PostList.as_view(), name="post-list"),
    path("posts/<int:pk>/", views.PostDetail.as_view()),
    path("users/", views.UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetail.as_view()),
    path("", views.api_root),
    path("posts/<int:pk>/body/", views.PostBody.as_view())
]