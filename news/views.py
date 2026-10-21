from django.shortcuts import render, get_object_or_404
from .models import Post

def news_list(request):
    news = Post.objects.filter(type=Post.NEWS).order_by('-created_at')
    return render(request, 'news_list.html', {'news': news})

def news_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news_detail.html', {'post': post})