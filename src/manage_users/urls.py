# myapp/urls.py
from django.urls import path, include
from manage_users.views.login_views import UserLoginView, UserRegisterView
from manage_users.views.user_views import *

urlpatterns = [
    path("user/", include([
        path('', AccountUserListView.as_view(), name='user-list'),
        path('create/', AccountUserCreateView.as_view(), name='user-create'),
        path('update/<uuid:pk>/', AccountUserUpdateView.as_view(), name='user-update'),
        path('delete/<uuid:pk>/', AccountUserDeleteView.as_view(), name='user-delete'),
    ])),

    path("api/", include([
        path('auth/', include([
            path('login/', UserLoginView.as_view(), name='login'),
            path('register/', UserRegisterView.as_view(), name='register'),
        ])),
    ])),
]
