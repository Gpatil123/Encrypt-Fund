from django.conf.urls import url
from Encrypt_fund import views

urlpatterns = [
    url(r'^', views.index),
    url(r'^Roadmap/', views.roadmap, name='Roadmap')
]