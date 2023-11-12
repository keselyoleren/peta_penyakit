"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from webbrowser import get
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from case.views.login_views import ChangePasswordAdminView, CustomPasswordChangeView, LogoutView, ProfileUserApiView, SignUpView, UserLoginView
from config.permis import LoginRequiredMixin
from django.views.i18n import JavaScriptCatalog


class IndexPage(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),    

    path("", IndexPage.as_view()),
    path("", include('manage_users.urls'), name="manage_users"),
    path("", include('case.urls'), name="case"),
    path("auth/", include([
        path("login/", UserLoginView.as_view(), name="login"),
        path("register/", SignUpView.as_view(), name="register"),
        path("logout/", LogoutView.as_view(), name="logout"),
        path("change-password/", CustomPasswordChangeView.as_view(), name="change-password"),
        path('change-password-admin/<int:user_id>/', ChangePasswordAdminView.as_view(), name="change-password-admin"),
        path('profile/', ProfileUserApiView.as_view(), name='profile'),
    ])),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)