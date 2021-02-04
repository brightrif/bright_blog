from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm

# Create your views here.

def homeview(request):

    qs = Post.objects.all() # queryset -> list of python object
    # if request.user.is_authenticated:
        # if User.objects.get(username=request.user).is_superuser: #check the logged in user is supper user or not 
        #     return redirect (reverse('account:dashboard'))
        # else:
    #         my_qs = Post.objects.filter(author=request.user)
    #         qs = (qs | my_qs).distinct()
    #         f_qs = Post.objects.filter(is_featured=True)[0]
    # else:
    # my_qs = Post.objects.all()
    # qs = (qs | my_qs).distinct()
    f_qs = Post.objects.filter(is_featured=True)[0]
    template_name = 'blog/home.html'
    context = {'object_list': qs, 'object_featured':f_qs}
    return render(request, template_name, context) 


def myposts(request):
    if request.user.is_authenticated:
        my_qs = Post.objects.filter(author=request.user)
    # qs = (qs | my_qs).distinct()
    else:
        return redirect('bloghome')
    template_name = 'blog/myposts.html'
    context = {'object_list': my_qs, }
    return render(request, template_name, context)

def blog_post_list_view(request):
    # list out objects 
    # could be search
   pass

def blogPostDetailView(request,slug):
    obj = get_object_or_404(Post, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context) 

# @login_required
#@staff_member_required
def post_create_view(request):
    # form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        form = PostForm(request.POST)
        author =  request.user
        if form.is_valid():
            print ('i came here')
            form.instance.author = author
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # form = PostForm()
            return redirect('bloghome')
    else:
        form = PostForm()
        template_name = 'blog/addpost.html'
        context = {'form': form}
    return render(request, template_name, context) 

# def post_create(request):
#     title = 'Create'
#     form = PostForm(request.POST or None, request.FILES or None)
#     author = get_author(request.user)
#     if request.method == "POST":
#         if form.is_valid():
#             form.instance.author = author
#             form.save()
#             return redirect(reverse("post-detail", kwargs={
#                 'id': form.instance.id
#             }))
#     context = {
#         'title': title,
#         'form': form
#     }
#     return render(request, "post_create.html", context)


def post_update(request, slug):
    title = 'Update'
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    author = request.user
    # if request.method == "POST":
    if form.is_valid():
        print ("coming here")
        form.instance.author = author
        form.save()
        return redirect(reverse("blogdetail", kwargs={
            'slug': form.instance.slug
        }))
        # return redirect (reverse('bloghome'))
    context = {
        'title': title,
        'form': form
    }
    return render(request, "blog/editpost.html", context)


