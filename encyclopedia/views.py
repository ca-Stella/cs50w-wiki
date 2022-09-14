from http.client import HTTPResponse
from xml.sax.handler import DTDHandler
from django.shortcuts import render

from . import util
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from markdown2 import Markdown
from django import forms
import random

class NewEntryForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'name':'title', 'style': 'width: 60%; text-align: left;'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'name': 'description', 'style': 'height: 12em; width: 60%;'}))

class EditForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'name': 'content'}))

def index(request):
    # render index.html by passing in list of entries
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title): 
    # Load markdown for convertion to HTML
    markdowner = Markdown()

    # Call the get_entry in util.py to load the markdown file
    page = util.get_entry(title)

    # If markdown page does not exist, render error page
    if page is None: 
        return render(request, "encyclopedia/dne_error.html", {
            "title": title
        })
    
    # If page exists, render the page
    return render(request, "encyclopedia/entry.html", {
        "page": markdowner.convert(page), 
        "title": title
    })


def search(request):
    search = request.GET.get('q','')
    entries = util.list_entries()
    page = util.get_entry(search)
    if page is None:
        matches = []
        for entry in entries: 
            if search.lower() in entry.lower(): 
                matches.append(entry)
        return render(request, "encyclopedia/search.html", {
            "matches": matches,
            "search": search
        })
    else: 
        return HttpResponseRedirect(reverse("entry", kwargs={"title":search}))

def new(request):
    if request.method == "POST":

        # Take in data submitted and save as form
        form = NewEntryForm(request.POST)

        # Check if form data is valid
        if form.is_valid(): 

            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

            if title in util.list_entries():
                return render(request, "encyclopedia/already_exists_error.html", {
                    "title": title
                })

            # Save the entry
            util.save_entry(title, content)

            return HttpResponseRedirect(reverse("entry", kwargs={"title":title}))

            
    # render new.html
    return render(request, "encyclopedia/new.html", {
        "form": NewEntryForm()
    })

def edit(request, title):
    page = util.get_entry(title)
    markdowner = Markdown()

    if request.method == "POST":

        # Take in data submitted and save as form
        form = EditForm(request.POST)

        # Check if form data is valid
        if form.is_valid(): 

            content = form.cleaned_data["content"]

            # Save the entry
            util.save_entry(title, content)

            return HttpResponseRedirect(reverse("entry", kwargs={"title":title}))

    # render edit.html
    return render(request, "encyclopedia/edit.html", {
        "form": EditForm(),
        "title": title, 
        "page": markdowner.convert(page)
    })

def randompg(request):
    markdowner = Markdown()

    num = random.randint(0, len(util.list_entries())- 1)
    title = util.list_entries()[num]
    page = util.get_entry(title)

    return render(request, "encyclopedia/entry.html", {
        "page": markdowner.convert(page), 
        "entry": title
    })