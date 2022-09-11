from django.shortcuts import render

from . import util

from markdown2 import Markdown

def index(request):
    # render index.html by passing in list of entries
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry): 
    # Load markdown for convertion to HTML
    markdowner = Markdown()

    # Call the get_entry in util.py to load the markdown file
    page = util.get_entry(entry)

    # If markdown page does not exist, render error page
    if page is None: 
        return render(request, "encyclopedia/dne_error.html", {
            "entry": entry
        })
    
    # If page exists, render the page
    return render(request, "encyclopedia/entry.html", {
        "page": markdowner.convert(page), 
        "entry": entry
    })