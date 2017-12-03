from django.conf.urls import url, include
from . import views
from allauth.account import views as allauth_views
# api endpoints

urlpatterns = [
    url(r"^companies/$", views.CompanyList.as_view(), name="company-list"),
    url(r"^jobs/$", views.ListingList.as_view(), name="job-list"),
    url(r"^company/(?P<pk>[0-9]+)/$", views.CompanyDetail.as_view(),
        name="company-detail"),
    url(r"job/(?P<pk>[0-9]+)/$", views.ListingDetail.as_view(),
        name="listing-detail"),

    # auth urls
    url(r'^auth/', include("rest_framework.urls",
                           namespace="rest_framework")),
    url(r'^rest-auth/', include("rest_auth.urls",
                                namespace="rest_auth")),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls',
                                             namespace="rest_auth.registration")),
]
