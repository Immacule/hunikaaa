from  django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views
from .views import *
urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('farmers', views.farmers, name="farmers"),
    path('farmers/<int:id>', views.farmersUpdate, name="farmers Update"),
    path('login', Login.as_view(), name="login"),
    path('agronome', AgronomeView.as_view(), name="agronome"),
    path('create', views.accountCreation, name="create")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
