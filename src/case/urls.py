# myapp/urls.py
from django.urls import path, include, re_path
from case.views.address_views import *
from case.views.case_api_views import CaseApiView, CaseListApiView, DeleteMultipleCaseView, ImportCaseView
from case.views.disease_view import *
from case.views.diseases_api_views import DiseasesApiView
from case.views.feedback_api_views import FeedbackApiView
from case.views.feedback_views import FeedbackListView
from case.views.province_view import *
from case.views.puskeswan_api_views import PueskeswanSubDistrictApiView, PueskeswanSubDistrictVillageApiView
from case.views.puskeswan_views import *
from case.views.regency_views import *
from case.views.subdistrict_views import *
from case.views.village_views import *
from case.views.case_views import *

from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'feedback', FeedbackApiView, basename='feedback-api')

url = route.urls

urlpatterns = [
    path("case/", include([
        path('', CaseListView.as_view(), name='case-list'),
        path('create/', CaseCreateView.as_view(), name='case-create'),
        path('update/<uuid:pk>/', CaseUpdateView.as_view(), name='case-update'),
        path('delete/<uuid:pk>/', CaseDeleteView.as_view(), name='case-delete'),
    ])),

    path("pueskeswan/", include([
        path('', PuskeswanListView.as_view(), name='puskeswan-list'),
        path('create/', PuskeswanCreateView.as_view(), name='puskeswan-create'),
        path('update/<uuid:pk>/', PuskeswanUpdateView.as_view(), name='puskeswan-update'),
        path('delete/<uuid:pk>/', PuskeswanDeleteView.as_view(), name='puskeswan-delete'),
    ])),
    path("disease/", include([
        path('', DiseaseListView.as_view(), name='disease-list'),
        path('create/', DiseaseCreateView.as_view(), name='disease-create'),
        path('update/<uuid:pk>/', DiseaseUpdateView.as_view(), name='disease-update'),
        path('delete/<uuid:pk>/', DiseaseDeleteView.as_view(), name='disease-delete'),
    ])),

    path("province/", include([
        path('', ProvinceListView.as_view(), name='province-list'),
        path('create/', ProvinceCreateView.as_view(), name='province-create'),
        path('update/<uuid:pk>/', ProvinceUpdateView.as_view(), name='province-update'),
        path('delete/<uuid:pk>/', ProvinceDeleteView.as_view(), name='province-delete'),
    ])),

    path("regency/", include([
        path('', RegencyListView.as_view(), name='regency-list'),
        path('create/', RegencyCreateView.as_view(), name='regency-create'),
        path('update/<uuid:pk>/', RegencyUpdateView.as_view(), name='regency-update'),
        path('delete/<uuid:pk>/', RegencyDeleteView.as_view(), name='regency-delete'),
    ])),

    path("subdistrict/", include([
        path('', SubDistrictListView.as_view(), name='subdistrict-list'),
        path('create/', SubDistrictCreateView.as_view(), name='subdistrict-create'),
        path('update/<uuid:pk>/', SubDistrictUpdateView.as_view(), name='subdistrict-update'),
        path('delete/<uuid:pk>/', SubDistrictDeleteView.as_view(), name='subdistrict-delete'),
    ])),

    path("village/", include([
        path('', VillageListView.as_view(), name='village-list'),
        path('create/', VillageCreateView.as_view(), name='village-create'),
        path('update/<uuid:pk>/', VillageUpdateView.as_view(), name='village-update'),
        path('delete/<uuid:pk>/', VillageDeleteView.as_view(), name='village-delete'),
    ])),

    path("feedback/",FeedbackListView.as_view(), name='feedback-list'),

    path('api/', include([
        path('address/', include([
            path("province/", ProvicnceViews.as_view(), name=""),
            path("regency/<uuid:province_id>/", RegencyApiView.as_view() , name=""),
            path("district/<uuid:regency_id>/", SubDistrictApiView.as_view() , name=""),
            path("village/<uuid:sub_district_id>/", VillageApiView.as_view() , name="")
        ])),

        path('puskeswan/', include([
            path('district/', PueskeswanSubDistrictApiView.as_view(), name='district-puskeswan'),
            path('district/village/', PueskeswanSubDistrictVillageApiView.as_view({"get":"list"}), name='district-village-puskeswan'),
            path('district/village/<uuid:sub_district_id>/', PueskeswanSubDistrictVillageApiView.as_view({'get':'retrieve'}), name='get-district-village-puskeswan'),
        ])),

        path('case/', include([
            path("", CaseApiView.as_view(), name="case"),
            path("list/", CaseListApiView.as_view(), name="case_list"),
            path("import/", ImportCaseView.as_view(), name="import-case"),
            path('diseases/', DiseasesApiView.as_view(), name='diseases'),
            path('delete-multiple-case/', DeleteMultipleCaseView.as_view(), name='delete-multiple-case'),
            path("delete/<uuid:case_id>/", CaseApiView.as_view(), name="delete-case"),
        ])),

        path("", include(url), name="")

    ]))
]
