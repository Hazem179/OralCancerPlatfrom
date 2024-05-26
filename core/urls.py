from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctor_list_create, name='doctor-list-create'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor-detail'),
    path('specializations/', views.specialization_list_create, name='specialization-list-create'),
    path('specializations/<int:pk>/', views.specialization_detail, name='specialization-detail'),
    path('certifications/', views.certification_list_create, name='certification-list-create'),
    path('certifications/<int:pk>/', views.certification_detail, name='certification-detail'),
    path('tags/', views.tag_list_create, name='tag-list-create'),
    path('tags/<int:pk>/', views.tag_detail, name='tag-detail'),
    path('posts/', views.post_list_create, name='post-list-create'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('post-tags/', views.post_tags_list_create, name='post-tags-list-create'),
    path('post-tags/<int:pk>/', views.post_tags_detail, name='post-tags-detail'),
    path('comments/', views.comment_list_create, name='comment-list-create'),
    path('comments/<int:pk>/', views.comment_detail, name='comment-detail'),
    path('videoblogs/', views.videoblog_list_create, name='videoblog-list-create'),
    path('videoblogs/<int:pk>/', views.videoblog_detail, name='videoblog-detail'),
    path('contacts/', views.contact_list_create, name='contact-list-create'),
    path('contacts/<int:pk>/', views.contact_detail, name='contact-detail'),
    # path('doctor-specializations/', views.doctor_specialization_list_create, name='doctor-specialization-list-create'),
    # path('doctor-specializations/<int:pk>/', views.doctor_specialization_detail, name='doctor-specialization-detail'),
    # path('doctor-certifications/', views.doctor_certification_list_create, name='doctor-certification-list-create'),
    # path('doctor-certifications/<int:pk>/', views.doctor_certification_detail, name='doctor-certification-detail'),
]
