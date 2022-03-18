from django.urls import path
from . import views as v
urlpatterns=[
    path('first/', v.first_view, name='firstview'),
    path('create/', v.create_form, name='createform'),
    path('view/', v.view_data, name='viewdata'),
    path('view/<int:ab>', v.single_data, name='single_data'),
    path('update/<int:ab>', v.update_data, name='update_data'),
    path('delete/<int:ab>', v.delete_data, name='delete_data'),
]


