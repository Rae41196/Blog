from .views import Postlist, post_detail
from django.urls import path

urlpatterns = [
    path('', Postlist.as_view(), name = 'home'),
    path('<slug:slug>/', post_detail, name='post_detail')
]

