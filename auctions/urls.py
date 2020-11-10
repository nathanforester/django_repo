from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("closed_listings", views.closed_listings, name="closed_listings"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listing/<int:listing_id>", views.listing_page, name="listing_page"),
    path("bidding/<int:id>", views.bidding, name="bidding"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add_to_watchlist/<int:listing_id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("watchlist_remove/<int:listing_id>", views.watchlist_remove, name="watchlist_remove"),
    path("end_listing/<int:listing_id>/<int:user_id>", views.end_listing, name="end_listing"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.category_listings, name="category_listings"),
    path("comments/<int:listing_id>", views.add_comments,  name="add_comments")
]
