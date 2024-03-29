from django.urls import path
from watchlist_app.api import views

urlpatterns = [
    path("watchlist/list", views.Watchlist, name="watchlist"),
    path("watchlist/<int:watch_id>", views.get_watchlist_by_id, name="get_watchlist_by_id"),
    path("platform/list", views.Platforms, name="platform"),
    path("platform/<int:watch_id>", views.get_platform_by_id, name="get_platform_by_id"),

    path("reviews/list", views.get_all_reviews, name="reviews"),
    path("reviews/<int:watch_id>", views.get_reviews_for_watchlist, name="get_reviews_for_watchlist"),

]


