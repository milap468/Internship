from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import Post,Like,Comment
from django.db.models import Q
from accounts.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    
    return render(request,'dashboard/index.html')

def posts(request):
   
    posts = Post.objects.all()
     
    return render(request,'dashboard/posts.html',{'posts':posts})

def post(request,post_id):

    post = Post.objects.get(pk=post_id)
    likes = Like.objects.filter(post=post_id)
    comments = Comment.objects.filter(post=post_id)
    count = 0
    for i in likes:
        count = count + 1


    return render(request,'dashboard/post.html',{'post':post,'count':count,'comments':comments})

def like(request,post_id):
    post = Post.objects.get(pk=post_id)
    try:

        like = Like.objects.filter(Q(post=post_id) and Q(user=request.user))[0]
        like.delete()
        return HttpResponseRedirect(reverse("post",kwargs={'post_id': post_id}))
    except:

        like = Like.objects.create(post=post,user=request.user,like_count=1)
        like.save()

        return HttpResponseRedirect(reverse("post",kwargs={'post_id': post_id}))
    
def comment(request,post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":

        content = request.POST.get('content')
        print(content)

        if content == "":

            return HttpResponseRedirect(reverse("post",kwargs={'post_id': post_id}))
        
        comment = Comment.objects.create(comment=content,post=post,user=request.user)
        comment.save()
        return HttpResponseRedirect(reverse("post",kwargs={'post_id': post_id}))


    return render(request,'dashboard/post.html')



def create_post(request):

    if request.method == "POST":

        title = request.POST.get("title")
        content = request.POST.get('post-content')

        if title == "" or content == "":

            return HttpResponseRedirect(reverse('create-post'))
        
        post = Post.objects.create(title=title,content=content,user=request.user)
        post.save()

        return HttpResponseRedirect(reverse("posts"))

    return render(request,'dashboard/create-post.html')

def profile(request):

    if request.method == "POST":

        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')


        print(first_name)
        print(username)
        print(email)
        print(phone)

        if first_name == "" or username == "" or email == "":

            return HttpResponseRedirect(reverse('profile'))
        
        user = User.objects.get(pk=request.user)
        user.first_name = first_name
        print(user.first_name)
        user.username = username
        user.email = email
        user.phone = phone
        user.save()

        return HttpResponseRedirect(reverse('profile'))


    user = User.objects.get(pk=request.user)

    return render(request,'dashboard/profile.html',{'user':user})

def change_password(request):
    
    if request.method == "POST":

        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        user = authenticate(email=request.user,password=current_password)

        if user:
            user.set_password(new_password)
            user.save()
            login(request,user)            
            return HttpResponseRedirect(reverse('profile'))
        else:

            return HttpResponseRedirect(reverse('profile'))