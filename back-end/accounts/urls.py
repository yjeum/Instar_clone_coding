from django.urls import path
from accounts import views

app_name = "accounts"
urlpatterns = [
    path("signup/", views.signup),
    path("login/", views.login),
    path("logout/", views.logout),
    path("update/", views.update),
    path("change_password/", views.change_password),
    path("delete/", views.delete),
    path("<username>/", views.profile, name="profile"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
    path("<username>/followers/", views.follower_list, name="follower_list"),
    path("<username>/following/", views.following_list, name="following_list"),
]
