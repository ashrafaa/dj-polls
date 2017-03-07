from django.conf.urls import url
from recipe import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    #patterns('*', r'^hello/', 'views.hello', name='hello'),
]
