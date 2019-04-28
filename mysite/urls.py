from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('language/<language_code>', views.ActivateLanguageView.as_view(), name='change_language')
]