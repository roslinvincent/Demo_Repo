from django.urls import path
from .views import AuthorListView,AuthorCreateView,AuthorDetailView,AuthorUpdateView,AuthorDeleteView

urlpatterns = [
     path("authors/", AuthorListView.as_view(), name="author-list"),
     path("authors/add/", AuthorCreateView.as_view(), name="author-add"),
    path("authors/detail/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("authors/<int:pk>/edit/", AuthorUpdateView.as_view(), name="author-edit"),
    path("authors/<int:pk>/delete/", AuthorDeleteView.as_view(), name="author-delete"),
]