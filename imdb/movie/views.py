from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie, MovieLink

# Create your views here.

class MovieList(ListView):
    model=Movie
    paginate_by=1


class MovieDetail(DetailView):
    model=Movie

    def get_object(self):
        obj=super().get_object()
        obj.views_count+=1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['links']=MovieLink.objects.filter(movie=self.get_object())
        context['realted_movies']=Movie.objects.filter(category=self.get_object().category)
        return context


class MovieCategory(ListView):
    model=Movie
    paginate_by=1

    def get_queryset(self):
        self.category=self.kwargs['category']
        return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['movie_category']=self.category
        return context


class MovieLanguage(ListView):
    model=Movie
    paginate_by=1

    def get_queryset(self):
        self.language=self.kwargs['lang']
        return Movie.objects.filter(language=self.language)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['movie_language']=self.language
        return context


class MovieSearch(ListView):
    model=Movie
    paginate_by=1

    def get_queryset(self):
        query=self.request.GET.get('query')
        if query:
            object_list=self.model.objects.filter(title__icontains=query)
        else:
            object_list=self.model.objects.none()
        return object_list


class MovieYear(YearArchiveView):
    queryset=Movie.objects.all()
    date_field='year_of_production'
    make_object_list=True
    allow_future=True
    print(queryset)
