
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.views.generic import TemplateView
from django.views.i18n import JavaScriptCatalog

from case.views.login_views import ChangePasswordAdminView, CustomPasswordChangeView, LogoutView, ProfileUserApiView, SignUpView, UserLoginView
from config.permis import LoginRequiredMixin

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
    ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



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

if settings.SWAGGER_ENABLED:
    urlpatterns += [
        url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)