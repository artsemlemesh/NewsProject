from datetime import datetime
from email.headerregistry import Group
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post, Category, PostCategory, Author

from django.contrib.auth.mixins import PermissionRequiredMixin


from django.db.models.signals import post_save
class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 4


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    #added below and pRM
    permission_required = ('application.add_post')

class PostUpdate(PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    # added below and pRM
    permission_required = ('application.change_post')

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')



class CategoryListView(PostList):
    model = Post
    template_name = 'news/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self, *args, **kwargs):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(categories=self.category) #.order_by('-created_at')
        #keys = self.kwargs.keys()
        #print('THIS IS A SELF.CATEGORY', keys)# not necessary
        #print('THIS IS A QUERYSET', queryset)           # not necessary
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        # print('CONTEXT category/', context['category'])
        # print('CONTEXT isnot sub/', context['is_not_subscriber'])
        return context



@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'you have successfully subscribed on category'
    return render(request, 'news/subscribe.html', {'category': category, 'message': message})

# @login_required
# def upgrade_me(request):
#     user = request.user
#     authors_group = Group.objects.get(name='authors')
#     if not request.user.groups.filter(name='authors').exists():
#         authors_group.user_set.add(user)
#     Author.objects.create(authorUser=user)
#     return redirect('/')

