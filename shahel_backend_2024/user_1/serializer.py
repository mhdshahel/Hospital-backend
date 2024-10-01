from rest_framework import serializers
from user_1.models import Doctors,staffs,patients,booking
  
class Doctorss(serializers.ModelSerializer):
    class Meta:
        model=Doctors
        fields='__all__'



class staffss(serializers.ModelSerializer):
    class Meta:
        model=staffs
        fields='__all__'



class patientss(serializers.ModelSerializer):
    class Meta:
        model=patients
        fields='__all__'