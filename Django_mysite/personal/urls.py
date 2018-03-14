from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index , name='index' ),#index jest tutaj opcjonalnym argumentem który można wykorzystywać do
    url(r'^contact', views.contact , name='contact' ),
    #name jest użyte tylko do identyfikacji, contact jest to metoda wewnatrz modulu views
]