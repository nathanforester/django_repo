from django.contrib.auth.models import AbstractUser
from django.db import models
import django.utils.timezone

# User table inherits from AbstractUser Django - built in user model, can add extra columns if needed
class User(AbstractUser):
    pass

class Listings(models.Model):

    listing_id      = models.AutoField(primary_key=True)
    user_id         = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    title           = models.CharField(max_length=1000)
    description     = models.CharField(max_length=1000)
    IMG_URL         = models.CharField(max_length=1000)
    category        = models.CharField(max_length=50, null=False, default='other')
    starting_price  = models.DecimalField(default=0.0, max_digits=11, decimal_places=2)
    current_price   = models.DecimalField(default=0.0, max_digits=11, decimal_places=2)
    start_date      = models.DateTimeField(auto_now=False, auto_now_add=False, default=django.utils.timezone.now)
    end_date        = models.DateTimeField(auto_now=False, auto_now_add=False, default=django.utils.timezone.now)
    is_sold         = models.BooleanField(default=False)

class Bids(models.Model):

    bid_id      = models.AutoField(primary_key=True)
    user_id     = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id  = models.ForeignKey(Listings, on_delete=models.CASCADE)
    bid_price   = models.DecimalField(max_digits=11, decimal_places=2)

    # used if printing row in python shell
    def __str__(self):
        return f"User: {self.user_id} bid on listing: {self.listing_id} with a price of {self.bid_price}"

class Comments(models.Model):

    comment_id  = models.AutoField(primary_key=True)
    user_id     = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id  = models.ForeignKey(Listings, on_delete=models.CASCADE)
    comment     = models.CharField(max_length=1000)

class Watchlist(models.Model):

    watchlist_id = models.AutoField(primary_key=True)
    user_id      = models.ForeignKey(User, on_delete=models.CASCADE)
    listing_id   = models.ForeignKey(Listings, on_delete=models.CASCADE)
    is_on_list   = models.BooleanField(default=True)
