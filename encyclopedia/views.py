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
    if request.method == "POST":
        entry = request.POST.get("q")
        # get all the strings that contains the entry substring
        entries = [x for x in list_entries() if entry.upper() in x.upper()]
        return render(
            request, "encyclopedia/search.html", {"q": entry, "entries": entries}
        )


def new(request):
    if request.method == "POST":
        entry = request.POST.get("title").upper()
        if entry in list_entries():
            return render(request, "encyclopedia/exist.html", {"entry": entry})
        desc = request.POST.get("description")
        save_entry(entry, desc)
        return HttpResponseRedirect(f"/wiki/{entry}")
    return render(request, "encyclopedia/new.html")


def edit(request, entry):
    content = get_entry(entry)
    if request.method == "POST":
        save_entry(entry, request.POST.get("content"))
        return HttpResponseRedirect(f"/wiki/{entry}")
    return render(
        request, "encyclopedia/edit.html", {"entry": entry, "content": content}
    )


def notFound(request):
    return render(request, "encyclopedia/notFound.html")
