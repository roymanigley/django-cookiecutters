from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from {{ cookiecutter.project_slug }} import views


settings.LOGIN_URL = '/login/'
settings.LOGIN_REDIRECT_URL = '/home/'
urlpatterns = [
      path('home/', login_required(views.home)),
      path('login/', LoginView.as_view(template_name='auth/login.html')),
      path('logout/', LogoutView.as_view(template_name='auth/logout.html')),
      path('', login_required(views.home)),
]

{% for model in cookiecutter.models.models_list %}urlpatterns += views.{{ model.name}}Form.urls()
{% endfor %}

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
