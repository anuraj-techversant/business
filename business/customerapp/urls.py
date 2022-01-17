"""
The urls.py contains url defined unser the customer app.
"""
from django.conf.urls import url
from customerapp import views

urlpatterns = [
    url('customer/$', views.CustomerView.as_view()),
    url('customer/(?P<pk>[0-9]+)/$', views.CustomerDescriptionDetail.as_view()),
]
