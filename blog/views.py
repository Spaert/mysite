from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .form import PostForm

def post_list(request):
    queryset_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list, 10)  # Show 10 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var" : page_request_var
    }
    return render(request, "list.html", context)


    # if request.user.is_authenticated():
    #
    #     context = {
    #         "object_list" : queryset,
    #         "title" : "my user list"
    #     }
    # else:
    #     context = {
    #         "object_list": queryset,
    #         "title" : "List"
    #     }
    #

def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance" : instance,
    }

    return render(request,"detail.html",context)


def post_create(request):
    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created!",extra_tags='success created')
        #message success
        return HttpResponseRedirect(instance.get_absolute_url())



    # if request.method == 'POST':
    #     print (request.POST.get("title"))
    #     print (request.POST.get("content"))
    context = {
        "form" : form
    }
    return render(request, "form.html", context)


def post_update(request, id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None,instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved",extra_tags='save')
        # message success
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title" : instance.title,
        "instance" : instance,
        "form": form
    }

    return render(request, "form.html", context)

def post_delete(request,id):
    instance = get_object_or_404(Post, id=id)
    messages.success(request, "Successfully deleted!")
    instance.delete()
    return redirect("post:list")



