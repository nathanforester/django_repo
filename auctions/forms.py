from django import forms

CATEGORY_CHOICES = (
    ('music','Music'),
    ('fashion', 'Fashion'),
    ('sporting_goods','Sporting Goods'),
    ('electronics','Electronics'),
    ('jewellery_and_watches','Jewellery & Watches'),
    ('motors','Motors'),
    ('toys_and_games','Toys & Games'),
    ('collectables_and_antiques','Collectables & Antiques'),
    ('home_and_garden','Home & Garden'),
    ('other','Other')
)

class ListingsForm(forms.Form):
    title = forms.CharField()
    category = forms.CharField(label="Cat-E-Gory",
    widget=forms.Select(choices=CATEGORY_CHOICES))
    description = forms.CharField()
    IMG_URL = forms.CharField()
    starting_price = forms.DecimalField()
    number_of_days = forms.IntegerField(min_value=3, max_value=7)

class BiddingForm(forms.Form):
    new_bid = forms.DecimalField()

class AddCommentForm(forms.Form):
    new_comment = forms.CharField()
