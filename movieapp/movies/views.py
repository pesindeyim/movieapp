from django.shortcuts import render
from .models import Category, Movie
# kategori_list={"macera", "romantik", "dram" , "bilim kurgu"}
# # film_list = [
#     {
#         "id":1,
#         "film_adi":"film 1",
#         "aciklama":"film 1 aciklama",
#         "resim":"1.jpeg",
#         "anasayfa":True
#         },
#     {   
#         "id":2,
#         "film_adi":"film 2",
#         "aciklama":"film 2 aciklama",
#         "resim":"2.jpeg",
#         "anasayfa":False
#         },
#     {   
#         "id":3,
#         "film_adi":"film 3",
#         "aciklama":"film 3 aciklama",
#         "resim":"3.jpeg",
#         "anasayfa":True
#         },
#     {   
#         "id":4,
#         "film_adi":"film 4",
#         "aciklama":"film 4 aciklama",
#         "resim":"4.jpeg",
#         "anasayfa":False
#         }
#     ]   
def home(request):
    data = {
        "kategoriler": Category.objects.all(), #kategori_list,
        "filmler": Movie.objects.filter(anasayfa=True) #film_list
        #filtreleme var anasayfaları true olanları ekleme
    }
    return render(request,"index.html", data)
def movies(request):
    data = {
        "kategoriler": Category.objects.all(), #kategori_list,
        "filmler": Movie.objects.all() #film_list
    }
    return render(request,"movies.html",data)
def moviedetails(request, id):
    data = {
        "movie":Movie.objects.get(id=id)
    }
    return render(request,"details.html",data)
