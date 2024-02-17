from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from .models import Blog


# Cache the blog_detail view for 2 minutes (7200 seconds)
@cache_page(7200)
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, "blog/blog_list.html", {"blogs": blogs})


# Cache the blog_detail view for 2 minutes (7200 seconds)
@cache_page(7200)
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, "blog/blog_detail.html", {"blog": blog})
