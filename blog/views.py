from django.shortcuts import render

# Create your views here

def post_list(request):
    return render(request, 'blog/post_list.html', {})

from django.shortcuts import render
from .models import Post
 


Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
 return render(request, 'blog/post_list.html', {})



