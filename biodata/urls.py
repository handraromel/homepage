from django.urls import path
from biodata.views import IndexView

from . import views

app_name = 'biodata'
urlpatterns = [
    path('', IndexView.as_view(), name='biodata'),
]
