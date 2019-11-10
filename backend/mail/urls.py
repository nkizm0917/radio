from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /mail/5/
    path('<int:mail_id>/', views.results, name='results'),
]
