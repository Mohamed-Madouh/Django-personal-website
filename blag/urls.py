from django.urls import path
from .views import all_post ,post_detail
app_name ='blag'

urlpatterns= [
    path('',all_post),
    path('<int:id >', post_detail)
]