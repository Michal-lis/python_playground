from django.conf.urls import url,include
from django.views.generic import ListView, DetailView
from blog.models import Film

urlpatterns=[
    url(r'^$',ListView.as_view(queryset=Film.objects.all().order_by("-date")[:25],
                               #od 0 do 25 to liczba postów
                               #tutaj proste view są opisane od razu w URL zamiast w pliku view
                               template_name="blog/blog.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Film,
                                             template_name='blog/post.html'))#primary key bedzie tutaj naszym ID postu
]