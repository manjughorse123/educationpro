from django.urls import path
from .views import *

urlpatterns = [
    
    path('teacher_info/', TeacherInfoView.as_view(), name='register_profile'),
    path('teach_profile_info/<int:pk>/', TeacherdetailInfoView.as_view(), name='tacherdetail'),
    path('teacher_biling_info/', TeacherBilingInfoView.as_view(), name='biling_info'),
    path('teacher_biling_info_detail/<int:pk>/', TeacherBilingdetailView.as_view(), name='biling_detail'),
    path('teacher_availability/', TeachAvailabilityView.as_view(), name='availability'),
    path('teacher_availability_detail/<int:pk>/', TeachAvailabilitydetailView.as_view(), name='availability_detail'),
    path('teacher_subject/', TeachSubjectView.as_view(), name='teach_subject'),
    path('teacher_subject_detail/<int:pk>/', TeachSubjectdetailView.as_view(), name='teach_subject_detail'),
    path('teacher_id_card/', TeachIDCardView.as_view(), name='teach_subject'),
    path('teacher_idcard_detail/<int:pk>/', TeachIDCarddetailView.as_view(), name='teach_subject_detail'),
    path('teacher_licences/', TeachLicencesView.as_view(), name='teach_licences'),
    path('teacher_Licences_detail/<int:pk>/', TeachLicencesdetailView.as_view(), name='teach_licences_detail'),
    path('teacher_vedio/', TeachVedioView.as_view(), name='teach_vedio'),
    path('teacher_vedio_detail/<int:pk>/', TeachVediodetailView.as_view(), name='teach_vedio_detail'),
    path('teacher_certificate/', TeachCertificateView.as_view(), name='teach_certificate'),
    path('teacher_certificate_detail/<int:pk>/', TeachCertificatedetailView.as_view(), name='teach_certificate_detail'),
    
]