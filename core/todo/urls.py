from django.urls import path
from . import views


app_name = 'todo'

urlpatterns = [
    path("", views.PostList.as_view(), name="post_list"),
    path("create/", views.PostCreateView.as_view(), name="post_create"),
    path("<int:pk>/edit/", views.PostEditView.as_view(), name="post_edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("<int:pk>/complete/", views.PostCompleteView.as_view(), name="post_complete"),
]
