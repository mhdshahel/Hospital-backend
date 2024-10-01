from django.urls import path
from .import views
urlpatterns=[
path('Register',views.Register_name,name='Register'),
path('Doctors',views.add_Doctors,name='doctors'),
path('staffs',views.add_staffs,name='staffs'),
path('patients',views.add_patients,name='patients'),
path('booking',views.add_booking,name='booking'),
path('delete',views.delete_multiple_data,name='delete_data'),
path('display',views.display_Doctors,name='display'),
path('search',views.search_for_doctor,name='search_for'),
path('for_staffs',views.search_for_staffs,name='search_for_staffs'),
path('for_patients',views.search_for_patients,name='search_for_patients'),
]
