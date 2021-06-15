from django.shortcuts import render
from django import forms
import random

# from django.urls import reverse
from markdown import markdown
from .util import list_entries, save_entry, get_entry
from django.http import HttpResponseRedirect


class EditEntry(forms.Form):
    body = forms.CharField(widget=forms.Textarea)


def index(request):
    entries = list_entries()
    return render(request, "encyclopedia/index.html", {"entries": entries})


def content(request, entry):
    a = get_entry(entry)
    # if there is no entry with that entry Name
    if a is None:
        return HttpResponseRedirect(f"/notfound")
    return render(
        request, "encyclopedia/entry.html", {"content": markdown(a), "entry": entry}
    )


def search(request):
    if request.method == "POST":
        entry = request.POST.get("q")
        # get all the strings that contains the entry substring
        entries = [x for x in list_entries() if entry.upper() in x.upper()]
        if len(entries) == 1 and entry.lower() == entries[0].lower():
            return HttpResponseRedirect(f"wiki/{entries[0]}")
        return render(
            request, "encyclopedia/search.html", {"q": entry, "entries": entries}
        )


def new(request):
    if request.method == "POST":
        title = request.POST.get("title")
        entry = [x for x in list_entries() if title.upper() == x.upper()]
        if len(entry) == 1:
            return render(request, "encyclopedia/exist.html", {"entry": entry[0]})
        desc = request.POST.get("description")
        save_entry(title, desc)
        return HttpResponseRedirect(f"/wiki/{title}")
    return render(request, "encyclopedia/new.html")


def edit(request, entry):
    content = get_entry(entry)
    if request.method == "POST":
        save_entry(entry, request.POST.get("content"))
        return HttpResponseRedirect(f"/wiki/{entry}")
    return render(
        request, "encyclopedia/edit.html", {"entry": entry, "content": content}
    )


def rndom(request):
    entries = list_entries()
    random_entry = random.choice(entries)
    return HttpResponseRedirect(f"/wiki/{random_entry}")


def notFound(request, exception):
    return render(request, "encyclopedia/notFound.html")
