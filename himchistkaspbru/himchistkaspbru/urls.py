import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from services.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('services.urls')),

    path('__debug__/', include(debug_toolbar.urls)),
]

handler404 = pageNotFound
