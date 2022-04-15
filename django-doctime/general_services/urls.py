from django.urls import path

from .views import (
        doctor_list,
        doctor_details,
        book_appoinment,
        change_appoinment_status,
        add_pescription,
        delete_appoinment,
        patient_pescription)


urlpatterns = [
    path('doctor_list/', doctor_list, name='doctor_list'),
    path('doctor_details/<int:id>/', doctor_details, name='doctor_details'),
    path('book_appoinment/<int:doctor_id>/', book_appoinment, name='book_appoinment'),
    path('change_appoinment_status/<int:id>/', change_appoinment_status, name='change_appoinment_status'),
    path('add_pescription/<int:id>/', add_pescription, name='add_pescription'),
    path('delete_appoinment/<int:id>/', delete_appoinment, name='delete_appoinment'),
    path('patient_pescription/<int:id>/', patient_pescription, name='patient_pescription'),
]