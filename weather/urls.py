from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^climate/', views.climate, name='climate'),
]