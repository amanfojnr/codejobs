from django.conf.urls import url
from . import views
# api endpoints

urlpatterns = [
    url(r"^companies/$", views.CompanyList.as_view(), name="company-list"),
    url(r"^jobs/$", views.ListingList.as_view(), name="job-list"),
    url(r"^company/(?P<pk>[0-9]+)/$", views.CompanyDetail.as_view(),
        name="company-detail"),
    url(r"job/(?P<pk>[0-9]+)/$", views.ListingDetail.as_view(),
        name="listing-detail"),
]

