from django.urls import path
from shop import views

urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('about/',views.about,name="AboutUs"),
    path('contect/',views.contect,name="ContectUs"),
    path('tracker/',views.tracker,name="TrakingStatus"),
    path('search/',views.search,name="search"),
    path('products/<int:myid>',views.productview,name="ProductView"),
    path('chekout/',views.chekout,name="Chekout"),
]
