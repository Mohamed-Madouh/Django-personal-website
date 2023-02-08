from django.urls import path
from .views import all_post ,post_detail ,postlist,postDetail
app_name ='blag'

urlpatterns= [
    path('',all_post),
    path('<int:id>', post_detail,name='post_detail'),
    path('cbv/', postlist.as_view()),
    path('cbv/<int:pk>', postDetail.as_view())
]