from django.urls import path
from enterprisems.views import IndexView

app_name = "enterprisems"

urlpatterns = [
    path("", IndexView.as_view(template_name="index.html"), name="index"),
]
