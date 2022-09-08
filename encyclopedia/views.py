from django.shortcuts import render

from . import util

from markdown2 import Markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title): 
    markdowner = Markdown()
    page = util.get_entry(title)
    return render(request, "encyclopedia/entry.html", {
        "page": markdowner.convert(page), 
        "title": title
    })