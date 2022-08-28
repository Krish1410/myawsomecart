from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 align='center'>Some Apps Their</h1><hr><h3 align='center'><a href='admin/'><b>ADMIN PANNEL</b></a></h3><hr><h4 align='center'><a align='center' href='shop/'>Shop</a></h4><br><br><h4 align='center'><a href='blog/' align='center' >Blog</a></h4>")