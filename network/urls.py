
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:username>", views.profile, name="profile"),
    path("following", views.following, name="following"),

    # API Routes
    path("followers/<str:username>/", views.get_followers, name="followers"),
    path("following/<str:username>/", views.get_following, name="following"),
    path("post-count/", views.get_post_count, name="get_post_count"),
    path("posts/", views.get_posts, name="get_posts")
]