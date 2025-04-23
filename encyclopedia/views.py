from django.shortcuts import render
from markdown2 import Markdown
import random
from . import util

def convert_mdfile(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
       return markdowner.convert(content)
        

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry_content = convert_mdfile(title)
    if entry_content == None:
        return render(request, "encyclopedia/notfound.html")
    else:   
        return render(request, "encyclopedia/entry.html", {
            "title":title,
            "content":entry_content
        })
    
def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        entry_content = convert_mdfile(entry_search)
        if entry_content == None:
            options = []
            entries = util.list_entries()
            for entry in entries:
                if entry_search.lower() in entry.lower():
                    options.append(entry)
            return render(request, "encyclopedia/search.html", {
                "search_title":entry_search,
                "options":options
            })
        else:
            return render(request, "encyclopedia/entry.html", {
                "title":entry_search,
                "content":entry_content
            }) 
        
def newpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        new_page = util.get_entry(title) 
        if new_page is not None:
            return render(request, "encyclopedia/error.html")
        else:
            util.save_entry(title, content)  
            new_html_page = convert_mdfile(title)
            return render(request, "encyclopedia/entry.html", {
                "title":title,
                "content":new_html_page
            })
        

def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title'] 
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title":title,
            "content":content
        })       
    
def changed(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_page = convert_mdfile(title)
        return render(request, "encyclopedia/entry.html", {
            "title":title,
            "content":html_page
        })
    
def random_entry(request):
    entries = util.list_entries()
    title = random.choice(entries)
    html_page = convert_mdfile(title)
    return render(request, "encyclopedia/entry.html", {
        "title":title,
        "content":html_page
    })