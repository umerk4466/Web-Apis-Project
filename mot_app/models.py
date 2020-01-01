from django.db import models

# user model.
class User(models.Model):
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    current_vehicle_reg_no = models.CharField(max_length=255,blank=True ,null=True)
    full_name = models.CharField(max_length=255,blank=True ,null=True)
    email = models.CharField(max_length=255,blank=True, null=True)
    # profile_img = field
    join_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username

# vehicle model.
class Vehicle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    manufacturer = models.CharField(max_length=255)
    millage = models.BigIntegerField()
    condition = models.TextField(blank=True, null=True)
    registration_year = models.IntegerField()
    registration_number = models.CharField(max_length=255)
    last_mot_date = models.DateField(blank=True, null=True)
    mot_due = models.DateField()
    insurance_due = models.DateField()
    vehicle_notes = models.TextField(blank=True, null=True)
    repair_needed_note = models.TextField(blank=True, null=True)
    # picture = field
    added_on = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.registration_number

# reminder model.
class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE,blank=True, null=True)
    reminder_note = models.TextField()
    date = models.DateField()
    extra_field = models.CharField(max_length=255,blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username