from django.urls import path
from posts import views

app_name = "posts"
urlpatterns = [
    path("", views.index),
    path("<int:pk>/", views.detail),
    path("create/", views.create, name="create"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:post_pk>/comment/create", views.comment_create),  # 댓글 작성
    path(
        "<int:post_pk>/comment/<int:comment_pk>/update", views.comment_update
    ),  # 댓글 수정
    path("<int:post_pk>/comment", views.comment),  # 댓글 보기
    path(
        "<int:post_pk>/comment/<int:comment_pk>/delete", views.comment_delete
    ),  # 댓글 삭제
    path("<int:post_pk>/commemet/<int:parent_id>", views.comment_create),  # 대댓글 작성
]
