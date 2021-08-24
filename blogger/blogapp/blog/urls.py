from .views import Bloghome
from django.urls import path

urlpatterns = [

    path("", Bloghome.as_view(), name="home")


]
