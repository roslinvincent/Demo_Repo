from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from library.models import Author

# Create your views here.

class AuthorListView(ListView):
    model=Author
    template_name="author/authorlist.html"
    context_object_name="authors"

#Create Author
class AuthorCreateView(CreateView):
    model = Author
    fields = ["name", "email", "is_active"]
    template_name = "author/authoradd.html"
    success_url = reverse_lazy("author-list")
    
class AuthorDetailView(DetailView):
    model = Author
    template_name = "author/authordetail.html"
    context_object_name = "author"
class AuthorUpdateView(UpdateView):
    model = Author
    fields = ["name", "email", "is_active"]
    template_name = "author/authoredit.html"
    success_url = reverse_lazy("author-list")
class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "author/authordelete.html"
    success_url = reverse_lazy("author-list")