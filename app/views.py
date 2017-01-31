from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(publish_date=timezone.now()).order_by('publish_date')
    return  render(request, 'app/post_list.html', {'posts': posts})

