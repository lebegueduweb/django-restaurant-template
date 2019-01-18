from django.shortcuts import render, get_object_or_404
from .models import Post, Service, Carousel, MotGerante

def index2(request):
    posts = Post.objects
    services = Service.objects
    carousels = Carousel.objects
    mots = MotGerante.objects
    return render(
        request,
        "carousel/index2.html",
                 context={'posts': posts,
                          'services': services,
                          'carousels':carousels,
                          'mots': mots},
    )

