from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Category, Tag, Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms.ContactForm import ContactForm
from blog.forms.PostForm import PostForm
from django.contrib import messages
import os
from django.conf import settings

# Create your views here.

def home(request):
    # tags = ["web", "frontend", "backend", "digital"]

    # for name in tags:
    #     tag=Tag()
    #     tag.name=name
    #     tag.description=f"Description de tag {name}"
    #     tag.save()
    title = "Hello world"
    posts = Post.objects.all()
    paginator = Paginator(posts,8)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except:
        posts = paginator.page(1)

    return render(request, 'blog/index.html', {'title':title, 'posts':posts})

def post(request):
    title = "Title: New Post 30"
    datas = [
        "Article 1",
        "Article 2",
        "Article 3",
        "Article 4",
        "Article 5",
    ]
    context = {
            "title":title, 
            "datas":datas
        }
    return render(request, 'blog/post.html', context)

def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/single_post.html', {'post':post})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message est envoyé avec succès !')
            return redirect('blog-contact')
    else:
        form=ContactForm()

    return render(request, 'blog/contact.html', {'form':form})

@login_required
def dashboard_post(request):
    posts = Post.objects.filter(author=request.user)
    paginator = Paginator(posts,8)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except:
        posts = paginator.page(1)

    context = {
        'posts':posts
    }
    return render(request, 'blog/dashboard/post_index.html', context)

@login_required
def dashboard_post_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/dashboard/post_view.html', {'post':post})

@login_required
def dashboard_post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post ajouté avec succès !")       
            return redirect('dashboard_post')
        else:
            messages.error(request, 'Veuillez vérifier tous les champs')
    else:
        form = PostForm()
    return render(request, 'blog/dashboard/post_new.html',{'form':form})

@login_required
def dashboard_post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        if request.POST.get('_method') == 'PUT':
            if post.image:
                    image_path = post.image.path
                    if(os.path.exists(image_path)):
                        os.remove(image_path)
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, "Post modifié avec succès !")       
                return redirect('dashboard_post')
            else:
                messages.error(request, 'Veuillez vérifier tous les champs')
        else:
            form = PostForm(instance=post)
    else:
        form = PostForm(instance=post)
    context = {
        'form':form,
        'post':post,
    }
    return render(request, 'blog/dashboard/post_new.html', context)

@login_required
def dashboard_post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # Vérifier si l'utilisateur actuel n'est pas l'auteur de l'article
    if post.author != request.user:
        # Si l'utilisateur actuel n'est pas l'auteur de l'article
        messages.success(request, "Vous n'êtes pas autorisé à supprimer ce poste.")
        return redirect('dashboard_post')   
     
    if request.method == 'POST':
        if request.POST.get('_method') == 'DELETE':
            if post.image:
                image_path = post.image.path
                if(os.path.exists(image_path)):
                    os.remove(image_path)
            post.delete()
            messages.success(request, 'Le post est supprimé avec succès !')
    return redirect('dashboard_post')    

