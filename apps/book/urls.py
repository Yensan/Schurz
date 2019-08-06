from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', list_books),
    url(r'^(\d+)$', book_detail)
]
