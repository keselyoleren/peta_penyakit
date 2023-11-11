# myapp/urls.py
from django.urls import path, include
from case.views.address_views import *
from case.views.disease_view import *
from case.views.province_view import *
from case.views.puskeswan_views import *
from case.views.regency_views import *
from case.views.subdistrict_views import *
from case.views.village_views import *

urlpatterns = [
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

    path('api/', include([
        path('address/', include([
            path("province/", ProvicnceViews.as_view(), name=""),
            path("regency/<uuid:province_id>/", RegencyApiView.as_view() , name=""),
            path("district/<uuid:regency_id>/", SubDistrictApiView.as_view() , name=""),
            path("village/<uuid:sub_district_id>/", VillageApiView.as_view() , name="")
        ]))
    ]))
]
