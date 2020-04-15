from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import RedirectView
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from .models import Post

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = "blog_posts"
    ordering =['-date']
    paginate_by = 6

class AboutView(ListView):
    model = Post
    template_name = 'blog/about.html'


class PostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    fields = ['title', 'text', 'picture']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def like_post(request):
    # post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post = get_object_or_404(Post, id=request.POST.get('id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('blog/like_section.html', context, request=request)
        return JsonResponse({'form': html})





