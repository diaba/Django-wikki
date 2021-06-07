from django.shortcuts import render
from django import forms

from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def newpage(request):
    if(request.method == "GET"):
        return render(request, "encyclopedia/newpage.html", {
            "form": NewPageForm
       })
    else:
        form = NewPageForm(request.POST)
        if(util.get_entry(form['title'].value()) == None):
            util.save_entry(form['title'].value(),  form['content'].value())
        else:
            return render( request, "encyclopedia/errorpage.html")
        return HttpResponseRedirect(reverse("index"))

    