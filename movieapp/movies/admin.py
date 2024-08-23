from django.contrib import admin
from .models import Category, Movie
# Register your models here.
admin.site.register(Category)     # belirlediklerimizi koyduktan sonra 
   # admin panelinde görüp giriş yapabiliyoruz. 
admin.site.register(Movie)