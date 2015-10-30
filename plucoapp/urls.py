from django.conf.urls import url, patterns
from plucoapp import views

urlpatterns = patterns ('',
    url(r'^$', views.index, name='index')
)
