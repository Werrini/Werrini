from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# errors
def not_found(request, *args, **kwargs):
    return render(request, 'not_found.html')

def server_error(request, *args, **kwargs):
    return render(request, 'server_error.html')

def permission_denied(request, *args, **kwargs):
    return render(request, 'permission_denied.html')

def bad_request(request, *args, **kwargs):
    return render(request, 'bad_request.html')


# errors

def home(request):
    posts = Post.objects.filter(active=True)
    return render(request, 'home.html', {'posts':posts[::-1][0:3]} )

def about(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = 'This message was sent by: '+ form.cleaned_data['from_email']+'\n'+ form.cleaned_data['message'] 
            try:
                send_mail(subject, message, 'werrini1@gmail.com', ['werrini1@gmail.com'], fail_silently=False)
            except BadHeaderError:
                messages.add_message(request, messages.ERROR, 'Invalid header found.')
            messages.add_message(request, messages.INFO, '  Sent! Thank you.')
            return redirect('about')
    return render(request, "about.html", {'form': form})



def blogs(request):
    posts = Post.objects.all()[::-1]
    page = request.GET.get('page')
    paginator = Paginator(posts, 6)

    if paginator.num_pages > 1:
        page_obj = paginator.get_page(page)
    else:
        page_obj = None

    try:
	    posts = paginator.page(page)
    except PageNotAnInteger:
	    posts = paginator.page(1)
    except EmptyPage:
	    posts = paginator.page(paginator.num_pages)


    context = {
        'posts':posts,
        'page_obj': page_obj
    }
 
    return render(request, 'blogs.html', context)


def blog(request, slug): #to be used as /blog/actual-blog
    post = Post.objects.get(slug=slug)

    context = {
        'post':post
    }
    return render(request, 'blog.html', context)



def podcasts(request):
    posts = Post.objects.filter(featured=True)

    context={
        'posts':posts,
    }

    return render(request, 'podcasts.html', context)

# def podcast(request, slug): #to be used as /podcast/actual-podcast
#     #template to be changed
#     return render(request, 'podcasts.html')

def category(request, slug):
    tag = Tag.objects.get(name=slug)
    posts = Post.objects.filter(tags=tag.id)

    page = request.GET.get('page')
    paginator = Paginator(posts, 6)

    if paginator.num_pages > 1:
        page_obj = paginator.get_page(page)
    else:
        page_obj =  None

    try:
	    posts = paginator.page(page)
    except PageNotAnInteger:
	    posts = paginator.page(1)
    except EmptyPage:
	    posts = paginator.page(paginator.num_pages)

    context = {
        'posts':posts,
        'tag':tag,
        'page_obj': page_obj
    }

    return render(request, 'category.html', context)