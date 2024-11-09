from django.urls import path
from .views import HomePageViews, AboutPagesView

urlpatterns = [
    path("", HomePageViews.as_view(), name= "home"),
    path("about/",AboutPagesView.as_view(), name= "about")
]