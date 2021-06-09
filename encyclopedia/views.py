from django.shortcuts import render
from django.urls.base import reverse
from django import forms

# from django.urls import reverse
from markdown import markdown
from .util import list_entries, save_entry, get_entry
from django.http import HttpResponseRedirect


class EditEntry(forms.Form):
    body = forms.CharField(widget=forms.Textarea)


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": list_entries()})


def content(request, entry):
    a = get_entry(entry)
    if a is None:
        return "No Entry with That Name"
    return render(
        request, "encyclopedia/entry.html", {"content": markdown(a), "entry": entry}
    )


def search(request):
    return render(request, "encyclopedia/search.html")


def new(request):
    return render(request, "encyclopedia/new.html")


def edit(request, entry):
    content = get_entry(entry)
    print(content)
    if request.method == "POST":
        save_entry(entry, content)
        return HttpResponseRedirect(reverse("wiki:index"))
    return render(
        request, "encyclopedia/edit.html", {"entry": entry, "content": content}
    )


def notFound(request):
    return render(request, "encyclopedia/notFound.html")
