from django.views import View
from django.views.generic import ListView, DetailView

import blog

from .forms import ShareForm
from .models import Post, Comment
from django.utils import timezone
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

# def main_page(request):
# posts = Post.objects.filter(status=Post.StatusChoices.PUBLISHED, publish_time__lte=timezone.now())
# return render(request, 'blog_t/main_page.html', {'posts': posts})
# # IT REPLACE WITH THE BLOGLISTVIEW CLASS


class BlogListView(ListView):
    template_name = 'blog_t/main_page.html'
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.filter(status=Post.StatusChoices.PUBLISHED)


# def detail_view(request, year, month, day, slug):
# post = get_object_or_404(Post, status=Post.StatusChoices.PUBLISHED, publish_time__year=year,
# publish_time__month=month, publish_time__day=day, slug=slug)
# return render(request, 'blog_t/blog-post.html', {'post': post})

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_t/blog-post.html'

    def get_object(self, queryset=None):
        return Post.objects.get(status=Post.StatusChoices.PUBLISHED,
                                publish_time__year=self.kwargs['year'],
                                publish_time__month=self.kwargs['month'],
                                publish_time__day=self.kwargs['day'],
                                slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data()
        context['comments'] = Comment.objects.filter(post=self.get_object(),approved=True)
        return context

# def main_page(request):
# return render(request, 'blog_t/main_page.html')

class SharePost(View):
    def get(self, request, pk):
        form = ShareForm()
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog_t/share.html', {'form': form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = ShareForm(request.POST)
        if form.is_valid():
            send_mail(
                'Sharing a post'.format(post.title),
                form.cleaned_data.get('comment'),
                form.cleaned_data.get('email'),
                [form.cleaned_data.get('to')],
                fail_silently=False,
            )
            return redirect(post.get_absolute_url())
        else:
            return render(request, 'blog_t/share.html', {'post': post, 'form': form})


def signup_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'registration/login.html', {'form': form })
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/blog')
        else:
            return render(request, 'registration/login.html', {'form': form })
