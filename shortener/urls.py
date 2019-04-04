from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register('shortcuts', views.ShortcutViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.home, name='home'),
    path('<int:id>', views.pass_trough, name='pass')
]