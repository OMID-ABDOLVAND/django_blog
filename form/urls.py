from django.urls import path
from form.views import form_test

urlpatterns = [
    path('', form_test)
]
