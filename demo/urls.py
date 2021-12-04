from django.contrib import admin

from django.urls import include, path
from django.views import generic
from material.frontend import urls as frontend_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', generic.RedirectView.as_view(url='/workflow/', permanent=False)),
    path('', include(frontend_urls))
]
