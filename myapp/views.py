from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post,Comment
from django.utils import timezone
import datetime
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def hello(request):
   yooyoo = datetime.datetime.now().date()
   dataset="babaji masti main aag lgegi basti main"
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "myapp/hello.html", {"today" : yooyoo,"data" : dataset,"days_of_week" : daysOfWeek})


def post_list(request):
    posts=Post.objects.filter(publish_date__lte = timezone.now()).order_by('-publish_date') #descending order of publish_Date
    return render(request,"myapp/post_list.html",{'posts': posts})

def post_details(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,"myapp/post_details.html",{'post': post})

@login_required
def post_new(request):

    if request.method =='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            #post.publish_date=timezone.now()
            post.save()
            return redirect('post_details' , pk=post.pk)

    else :
        form=PostForm()

    return render(request,"myapp/post_edit.html",{'form':form})


@login_required
def post_edit(request,pk):
    post=get_object_or_404(Post,pk=pk)

    if request.method=='POST':
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.publish_date=timezone.now()
            post.save()

            return redirect('post_details', pk=post.pk)

    else :
      form = PostForm(instance=post)

    return render(request,"myapp/post_edit.html",{'form':form})


@login_required
def post_draft_list(request):
    posts=Post.objects.filter(publish_date__isnull=True).order_by('created_date')
    return render(request,'myapp/draft_posts.html',{'posts':posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('myapp.views.post_details', pk=pk)

@login_required
def post_remove(request, pk):
    post =  get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('myapp.views.post_list')


def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)

    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('myapp.views.post_details',pk=post.pk)
    else:
        form=CommentForm()

    return render(request,'myapp/add_comment_to_post.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('myapp.views.post_details', pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment, pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('myapp.views.post_details', pk=post_pk)
