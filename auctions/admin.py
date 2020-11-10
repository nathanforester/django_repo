from django.contrib import admin
from .models import User, Listings, Bids, Comments, Watchlist

# admin user interface can be used to view, add, edit, delete from tables
# Use 'python manage.py createsuperuser' to create a superuser logged_in_user
# access admin page using '/admin'
# Register your models here.

admin.site.register(User)
admin.site.register(Listings)
admin.site.register(Bids)
admin.site.register(Comments)
admin.site.register(Watchlist)
