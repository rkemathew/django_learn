from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.
def main_page(request):
    return render(request, "main_page.html", { "user": request.user })

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('Requested user not found.')

    bookmarks = user.bookmark_set.all()
    return render(request, "user_page.html", {
        "username": username,
        "bookmarks": bookmarks
    })

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")
