from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
# def home(request):
#     context ={
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html',context)

# def about(request):
#     return render(request, 'blog/about.html')


class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # def get_success_url(self):
    #     # Redirect to the detail view of the created post
    #     return reverse_lazy("blog-detail", kwargs={'pk': self.object.pk})

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    # def get_success_url(self):
    #         # Redirect to the detail view of the created post
    #     return reverse_lazy("blog-detail", kwargs={'pk': self.object.pk})

    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    def get_success_url(self):
        # Redirect to the detail view of the created post
        return reverse_lazy("blog-home")