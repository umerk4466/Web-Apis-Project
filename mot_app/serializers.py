from rest_framework import serializers
# import model
from mot_app.models import User
from mot_app.models import Vehicle
from mot_app.models import Reminder




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username', 'password', 'current_vehicle_reg_no','join_date',]
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'




class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'

