# 配置JWT接口(urls.py)

from django.urls import path, re_path
from rest_framework_simplejwt.tokens import RefreshToken
from web.views.index import index
from web.views.user.account.get_user_info import GetUserInfoView
from web.views.user.account.login import LoginView
from web.views.user.account.lougout import LogoutView
from web.views.user.account.refresh_token import RefreshTokenView
from web.views.user.account.register import RegisterView

urlpatterns = [
    path('api/user/account/login/', LoginView.as_view()),
    path('api/user/account/logout/', LogoutView.as_view()),
    path('api/user/account/register/', RegisterView.as_view()),
    path('api/user/account/refresh_token/', RefreshTokenView.as_view()),
    #将刚刚打包的前端页面index指到刚刚web.views.index的index函数去

    path('api/user/account/get_user_info/', GetUserInfoView.as_view()),

    path('', index),

    re_path(r'^(?!media/|static/|assets/).*$', index)
]
