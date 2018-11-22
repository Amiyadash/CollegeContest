from django.conf.urls import url
from .views import ContestView

urlpatterns=[
            url(r'^contest/$',ContestView.as_view()),
            ]
