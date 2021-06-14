from django.urls import path

from .views import index, content, search, new, edit, rndom

app_name = "wiki"

urlpatterns = [
    path("", index, name="index"),
    path("wiki/<str:entry>", content, name="entry"),
    path("search", search, name="search"),
    path("new", new, name="new"),
    path("wiki/edit/<str:entry>", edit, name="edit"),
    path("random", rndom, name="random"),
]
