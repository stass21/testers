from django.conf.urls import url
from new_test import views

urlpatterns = [url(r'^$', views.index, name='index'),

]