from django.conf.urls import url
from . import views


urlpatterns = [
    # /categories/
    url(r'^$', views.index, name="index"),

    # /categories/1/
    url(r'^(?P<cat_id>[0-9]+)/$', views.category, name='category'),
]