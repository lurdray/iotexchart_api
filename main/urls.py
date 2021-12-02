from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),

	path("get-iotex-usdt/", views.ChartOne, name="chart_one"),

]
