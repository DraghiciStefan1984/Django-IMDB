from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, MovieLink

# Create your views here.

class MovieList(ListView):
    model=Movie
    paginate_by=1


class MovieDetail(DetailView):
    model=Movie

    def get_object(self):
        return super(MovieDetail, self).get_object()

    def get_context_data(self, **kwargs):
        context=super(MovieDetail, self).get_context_data(**kwargs)
        context['links']=MovieLink.objects.filter(movie=self.get_object())
        return context