from django.shortcuts import render

from . import util

from markdown2 import Markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry): 
    markdowner = Markdown()
    page = util.get_entry(entry)
    if page is None: 
        return render(request, "encyclopedia/dne_error.html", {
            "entry": entry
        })
    return render(request, "encyclopedia/entry.html", {
        "page": markdowner.convert(page), 
        "entry": entry
    })