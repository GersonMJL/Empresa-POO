from django.urls import path
from django.views.generic import TemplateView


app_name = "enterprisems"

urlpatterns = [
    path(
        "", TemplateView.as_view(template_name="enterprisems/index.html"), name="index"
    ),
]
