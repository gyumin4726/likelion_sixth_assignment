from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', user_profile, name='user_profile'),  # 프로필 페이지 URL 추가
    path('profile/edit/', user_update, name='user_update'),  # 프로필 수정 페이지 URL 추가
]
