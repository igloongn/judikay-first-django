from django.urls import path
from . import views as v
urlpatterns=[
    path('first/', v.first_view, name='firstview'),
    path('create/', v.create_form, name='createform'),
    path('view/', v.view_data, name='viewdata'),
]


