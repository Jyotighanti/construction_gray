"""
URL configuration for Am project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Am_app import views



urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.index, name='index'),
     path('login', views.login, name='login'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
path('about', views.about, name='about'),
    path('service', views.service, name='service'),
    path('Service_image', views.Service_image, name='Service_image'),
    path('upload_service_image', views.upload_service_image, name='upload_service_image'),
    path('service_view', views.service_view, name='service_view'),
    path('service_view1', views.service_view1, name='service_view1'),



    path('building', views.building, name='building'),
    path('upload_building_image', views.upload_building_image, name='upload_building_image'),
    path('building_view', views.building_view, name='building_view'),
    path('building_view1', views.building_view1, name='building_view1'),
    path('delete_building/<int:image_id>/', views.delete_building, name='delete_building'),


    path('structural', views.structural, name='structural'),
    path('upload_structural_image', views.upload_structural_image, name='upload_structural_image'),
    path('structural_view', views.structural_view, name='structural_view'),
    path('structural_view1', views.structural_view1, name='structural_view1'),
    path('delete_strutural/<int:image_id>/', views.delete_strutural, name='delete_strutural'),



    path('elevation', views.Elevation, name='elevation'),
    path('upload_Elevation_image', views.upload_Elevation_image, name='upload_Elevation_image'),
    path('elevation_view', views.elevation_view, name='elevation_view'),
    path('elevation_view1', views.elevation_view1, name='elevation_view1'),


    path('renovation', views.renovation, name='renovation'),
    path('upload_renovation_image', views.upload_renovation_image, name='upload_renovation_image'),
    path('renovation_view', views.renovation_view, name='renovation_view'),
    path('renovation_view1', views.renovation_view1, name='renovation_view1'),
path('delete_renovation/<int:image_id>/', views.delete_renovation, name='delete_renovation'),

    path('swimming', views.swimming, name='swimming'),
    path('upload_swimming_image', views.upload_swimming_image, name='upload_swimming_image'),
    path('swimming_view', views.swimming_view, name='swimming_view'),
    path('swimming_view1', views.swimming_view1, name='swimming_view1'),
                  path('delete_swimming/<int:image_id>/', views.delete_swimming, name='delete_swimming'),

    path('freelancing', views.freelancing, name='freelancing'),
    path('upload_freelancing_image', views.upload_freelancing_image, name='upload_freelancing_image'),
    path('freelancing_view', views.freelancing_view, name='freelancing_view'),
    path('freelancing_view1', views.freelancing_view1, name='freelancing_view1'),
path('delete_freelancing/<int:image_id>/', views.delete_freelancing, name='delete_freelancing'),


    path('joinventure', views.joinventure, name='joinventure'),
    path('upload_joinventure_image', views.upload_joinventure_image, name='upload_joinventure_image'),
    path('joinventure_view', views.joinventure_view, name='joinventure_view'),
    path('joinventure_view1', views.joinventure_view1, name='joinventure_view1'),
     path('delete_join/', views.delete_join, name='delete_join'),

    path('landscape', views.landscape, name='landscape'),
    path('upload_landscape_image', views.upload_landscape_image, name='upload_landscape_image'),
    path('landscape_view', views.landscape_view, name='landscape_view'),
    path('landscape_view1', views.landscape_view1, name='landscape_view1'),
path('delete_land/', views.delete_land, name='delete_land'),


    path('fabrication', views.fabrication, name='fabrication'),
    path('upload_fabrication_image', views.upload_fabrication_image, name='upload_fabrication_image'),
    path('fabrication_view', views.fabrication_view, name='fabrication_view'),
    path('fabrication_view1', views.fabrication_view1, name='fabrication_view1'),
path('delete_fab/', views.delete_fab, name='delete_fab'),


    path('paintcontract', views.paintcontract, name='paintcontract'),
    path('upload_contract_image', views.upload_contract_image, name='upload_contract_image'),
    path('paintcontract_view', views.paintcontract_view, name='paintcontract_view'),
    path('paintcontract_view1', views.paintcontract_view1, name='paintcontract_view1'),

     path('retro_fitting', views.retro_fitting, name='retro_fitting'),
    path('upload_paintcontract_image', views.upload_paintcontract_image, name='upload_paintcontract_image'),
    path('retro_fitting_view', views.retro_fitting_view, name='retro_fitting_view'),
    path('retro_fitting_view1', views.retro_fitting_view1, name='retro_fitting_view1'),
path('delete_retro/', views.delete_retro, name='delete_retro'),

    path('completed_project', views.completed_project, name='completed_project'),
    path('upload_completed_project', views.upload_completed_project, name='upload_completed_project'),
    path('completed_project_view', views.completed_project_view, name='completed_project_view'),
     path('completed_project_view1', views.completed_project_view1, name='completed_project_view1'),
                  path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),


    path('ongoing_project', views.ongoing_project, name='ongoing_project'),
    path('upload_ongoing_project', views.upload_ongoing_project, name='upload_ongoing_project'),
    path('ongoing_project_view', views.ongoing_project_view, name='ongoing_project_view'),
    path('ongoing_project_view1', views.ongoing_project_view1, name='ongoing_project_view1'),
                  path('delete_project/', views.delete_project, name='delete_project'),
path('delete_oproject/', views.delete_oproject, name='delete_oproject'),

    path('dop', views.dop, name='dop'),
    path('upload_dop', views.upload_dop, name='upload_dop'),
path('dop_view', views.dop_view, name='dop_view'),
    path('dop_view1', views.dop_view1, name='dop_view1'),



 path('certificate', views.certificate, name='certificate'),
    path('upload_certificate', views.upload_certificate, name='upload_certificate'),
path('certificate_view1', views.certificate_view1, name='certificate_view1'),
    path('certificate_view', views.certificate_view, name='certificate_view'),

 path('epf', views.epf, name='epf'),
    path('upload_epf', views.upload_epf, name='upload_epf'),
path('epf_view1', views.epf_view1, name='epf_view1'),
    path('epf_view', views.epf_view, name='epf_view'),



 path('iso', views.iso, name='iso'),
    path('upload_iso', views.upload_iso, name='upload_iso'),
path('iso_view1', views.iso_view1, name='iso_view1'),
    path('iso_view', views.iso_view, name='iso_view'),



 path('lei', views.lei, name='lei'),
    path('upload_lei', views.upload_lei, name='upload_lei'),
path('lei_view1', views.lei_view1, name='lei_view1'),
    path('lei_view', views.lei_view, name='lei_view'),


 path('msme', views.msme, name='msme'),
    path('upload_msme', views.upload_msme, name='upload_msme'),
path('msme_view1', views.msme_view1, name='msme_view1'),
    path('msme_view', views.msme_view, name='msme_view'),



 path('esic', views.esic, name='esic'),
    path('upload_esic', views.upload_esic, name='upload_esic'),
path('esic_view1', views.esic_view1, name='esic_view1'),
    path('esic_view', views.esic_view, name='esic_view'),


 path('certificate', views.certificate, name='certificate'),
 path('delete_certificate/<int:certificate_id>/', views.delete_certificate, name='delete_certificate'),
    path('upload_listofmachine', views.upload_listofmachine, name='upload_listofmachine'),
path('listofmachine_view1', views.listofmachine_view1, name='listofmachine_view1'),
    path('listofmachine_view', views.certificate_view, name='listofmachine_view'),





                  path('gallery', views.gallery, name='gallery'),
                  path('upload_gallery_image', views.upload_gallery_image, name='upload_gallery_image'),
                  path('gallery_view', views.gallery_view, name='gallery_view'),
                  path('gallery_view1', views.gallery_view1, name='gallery_view1'),
                  path('delete_gallery/<int:image_id>/', views.delete_gallery, name='delete_gallery'),
path('job_application_view', views.job_application_view, name='job_application_view'),
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
