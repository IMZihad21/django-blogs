from django.shortcuts import render
from django.views.generic import View

from blog.models import Post


class Home(View):
    def get(self, request, *args, **kwargs):
        blogs = Post.objects.filter(status="PUBLISH")[:5]
        context = {"page_title": "Home", "blogs": blogs}
        return render(request, "blog/index.html", context)


class Details(View):
    def get(self, request, *args, **kwargs):
        blog_slug = kwargs["blog_slug"]
        blog = Post.objects.get(status="PUBLISH", slug=blog_slug)
        context = {"page_title": blog.title, "blog": blog}
        return render(request, "blog/details.html", context)
