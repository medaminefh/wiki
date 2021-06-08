from django.shortcuts import render
from markdown import markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def content(request, entry):
    a = util.get_entry(entry)
    print(entry, a)
    if a is None:
        return "No Entry with That Name"
    return render(request, "encyclopedia/entry.html", {
        "content": a
    })


def random(request):
    return render(request, "encyclopedia/search.html")


def search(request):
    return render(request, "encyclopedia/search.html")


def new(request):
    return render(request, "encyclopedia/new.html")


def edit(request):
    return render(request, "encyclopedia/edit.html")


def notFound(request):
    return render(request, "encyclopedia/notFound.html")
