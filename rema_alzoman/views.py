from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import Post
def home(request):
    posts = Post.objects.all()

    return render(request, 'rema_alzoman_index.html', context={'posts': posts})


from .forms import PostForm
def post_create(request):
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            return redirect('rema_alzoman:home')
    else:
        return render(request, 'post_create.html',context={'form':PostForm()})

def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('rema_alzoman:home')

