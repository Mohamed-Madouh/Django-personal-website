from django.shortcuts import render
from .models import post
from django.views.generic import ListView,DetailView
# Create your views here.
def all_post (request ):
    objects =post.objects.all()
    return render(request, 'blag/post_list.html',{'posts':objects})



def post_detail ( request , id ):
    object= post.objects.get(id=id)
    return render(request, 'blag/post_detal.html',{'post':object})



class postlist(ListView):
    model = post
class postDetail(DetailView):
    model = post