"""
URL configuration for untitled project.

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
from django.urls import path

from myapp import views

urlpatterns = [
    path('login/', views.login),
    path('login_Post/', views.login_Post),
    path('logout/', views.logout),
    path('Admin_home/', views.home),
    path('Admin_change_password/', views.Admin_change_password),
    path('Admin_change_password_post/', views.Admin_change_password_post),
    path('view_pending_Drivers/', views.view_pending_Drivers),
    path('driver_pending_post/', views.driver_pending_post),
    path('view_approved_Drivers/', views.view_approved_Drivers),
    path('Search_Approved_driver_post/', views.Search_Approved_driver_post),
    path('approve_Driver/<id>', views.approve_Driver),
    path('reject_Driver/<id>', views.reject_Driver),
    path('view_rejected_Drivers/', views.view_rejected_Drivers),
    path('Search_rejected_pg_post/', views.Search_rejected_pg_post),
    path('adm_view_ambulance/', views.adm_view_ambulance),
    path('adm_view_ambulance_post/', views.adm_view_ambulance_post),
    path('adm_approve_ambulance/<id>', views.adm_approve_ambulance),
    path('adm_reject_ambulance/<id>', views.adm_reject_ambulance),
    path('adm_view_approved_ambulance/', views.adm_view_approved_ambulance),
    path('adm_view_approved_ambulance_post/', views.adm_view_approved_ambulance_post),
    path('adm_view_rejected_ambulance/', views.adm_view_rejected_ambulance),
    path('adm_view_rejected_ambulance_post/', views.adm_view_rejected_ambulance_post),
    path('adm_view_users/', views.adm_view_users),
    path('adm_view_users_post/', views.adm_view_users_post),
    path('adm_view_complaint/', views.adm_view_complaint),
    path('adm_view_complaint_post/', views.adm_view_complaint_post),
    path('adm_send_reply/<id>', views.adm_send_reply),
    path('adm_send_reply_post/', views.adm_send_reply_post),
    path('adm_view_feedback/', views.adm_view_feedback),
    path('adm_view_feedback_post/', views.adm_view_feedback_post),




    path('and_login/', views.and_login),
    path('driver_signup_post/', views.driver_signup_post),
    path('driver_view_profile/', views.driver_view_profile),
    path('driver_edit_profile/', views.driver_edit_profile),
    path('driver_view_request/', views.driver_view_request),
    path('driver_view_approved_request/', views.driver_view_approved_request),
    path('driver_view_rejected_request/', views.driver_view_rejected_request),
    path('driver_approve_request/', views.driver_approve_request),
    path('driver_get_user_location/', views.driver_get_user_location),
    path('driver_reject_request/', views.driver_reject_request),
    path('driver_view_payments/', views.driver_view_payments),
    path('driver_change_password/', views.driver_change_password),
    path('driver_view_user_payment/', views.driver_view_user_payment),

    path('ambulance_driver_signup_post/', views.ambulance_driver_signup_post),
    path('ambulance_view_profile/', views.ambulance_view_profile),
    path('ambulance_edit_profile_post/', views.ambulance_edit_profile_post),
    path('ambulance_change_password/', views.ambulance_change_password),
    path('ambulance_view_request/', views.ambulance_view_request),
    path('ambulance_approve_request/', views.ambulance_approve_request),
    path('ambulance_reject_request/', views.ambulance_reject_request),
    path('ambulance_view_approved_request/', views.ambulance_view_approved_request),
    path('ambulance_get_user_location/', views.ambulance_get_user_location),
    path('ambulance_view_rejected_request/', views.ambulance_view_rejected_request),
    path('ambulance_view_user_payment/', views.ambulance_view_user_payment),



    path('user_signup_post/', views.user_signup_post),
    path('user_view_profile/', views.user_view_profile),
    path('user_edit_profile/', views.user_edit_profile),
    path('user_view_cab/', views.user_view_cab),
    path('user_view_cab_more/', views.user_view_cab_more),
    path('user_send_request/', views.user_send_request),
    path('user_view_request_status/', views.user_view_request_status),
    path('user_send_cab_payment/', views.user_send_cab_payment),
    path('user_view_cab_payment/', views.user_view_cab_payment),
    path('user_get_driver_location/', views.user_get_driver_location),
    path('user_view_request_status_more/', views.user_view_request_status_more),

    path('user_change_password/', views.user_change_password),
    path('user_send_complaint/', views.user_send_complaint),
    path('user_view_complaint_post/', views.user_view_complaint_post),
    path('user_feedback_post/', views.user_feedback_post),
    path('user_view_feedback_post/', views.user_view_feedback_post),

    path('user_view_ambulance/', views.user_view_ambulance),
    path('user_view_ambulance_more/', views.user_view_ambulance_more),
    path('user_send_ambulance_request/', views.user_send_ambulance_request),
    path('user_view_ambulance_request_more/', views.user_view_ambulance_request_more),
    path('user_view_ambulance_status/', views.user_view_ambulance_status),
    path('user_send_ambu_payment/', views.user_send_ambu_payment),
    path('user_view_ambu_payment/', views.user_view_ambu_payment),
    path('user_get_ambulance_location/', views.user_get_ambulance_location),
    path('_update_location/', views._update_location),


]
