from django.db.models.lookups import PostgresOperatorLookup
from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, ListView
from.models import Post
# Create your views here.


class Bloghome(ListView):
    model = Post

    template_name = "blog/index.html"
