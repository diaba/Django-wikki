from re import T
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
import random
from django.urls import reverse

from . import util


class NewPageForm(forms.Form):
    title = forms.CharField(label="Title", required="true")
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}), required="true")


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def webpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/webpage.html", {
            "form": NewPageForm
        })
    else:
        form = NewPageForm(request.POST)
        if util.get_entry(form['title'].value()) is None:
            util.save_entry(form['title'].value(), form['content'].value())
        else:
            return render(request, "encyclopedia/errors.html")
        return HttpResponseRedirect(reverse("index"))


def entrypage(request, title):
    if request.method == "POST":
        print(request.POST['title'])
        title = request.POST['title']
        entry = util.get_entry(title)
        if util.get_entry(request.POST['title']) is None:
            return render(request, "encyclopedia/error404s.html")
        else:
            return render(request, "encyclopedia/entrypage.html", {
                "entry": util.get_entry(title)})
    else:
        return render(request, "encyclopedia/entrypage.html", {
            "entry": util.get_entry(title)})


def search(request):
    if request.method == "POST":
        list = []
        txtsearch = request.POST['q']
        for txt in util.list_entries():
            if txtsearch.capitalize() in txt.capitalize():
                list.append({'entry':util.get_entry(txt),'title':txt})
        return render(request, "encyclopedia/search.html", {
            "entries": list,
            "textsearch":txtsearch
            })
    else:
        return render(request, "encyclopedia/search.html")

def randompage(request):
    title = random.choice(util.list_entries())
    return render(request, "encyclopedia/randompage.html", {
            "entry": util.get_entry(title),
            "title": title})
