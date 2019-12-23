from django.db import models
from django.contrib.auth.models import User


class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    timings = models.CharField(max_length=50)
    subjects = models.CharField(max_length=50)
    classes_taught = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    class_frequency = models.CharField(max_length=50)
    about = models.TextField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return self.name

class School(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_of_school = models.CharField(max_length=250, null=True)
    Address_of_School = models.TextField(max_length=250)
    mode = models.CharField(max_length = 50)
    Type = models.CharField(max_length=20)
    from_class = models.CharField(max_length = 50)
    Communicating_facilities = models.CharField(max_length=250)
    Available_streams_after_10th = models.CharField(max_length=250)
    Type_of_board = models.CharField(max_length = 50,null=True)
    Total_Students = models.CharField(max_length=50)
    safety_and_Securtiy_Measures = models.CharField(max_length=250)
    CCTV = models.CharField(max_length=50)
    students_per_teacher = models.CharField(max_length=50)
    Mention = models.CharField(max_length=50)
    Punishable_offence_include = models.CharField(max_length=100,null=True)
    Total_teachers = models.CharField(max_length=50)
    general_fee_structure = models.CharField(max_length=250)
    sports_played = models.CharField(max_length=50)
    Qualification_details_of_teachers = models.CharField(max_length=250)
    Facilities_provided = models.CharField(max_length=250)
    Major_achievements = models.CharField(max_length=150)
    Glorious_alumni_network = models.CharField(max_length=150)
    Teaching_ideology = models.CharField(max_length=150)
    Future_plans_and_developments = models.CharField(max_length=50)
    support_any_extra_activities_apart_from_curriculum = models.CharField(max_length=150)
    Principal_message = models.CharField(max_length=150)


    def __str__(self):
        return self.name_of_school

class Coaching(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_of_coaching = models.CharField(max_length=250, null=True)
    Address_of_coaching = models.TextField(max_length=250)
    mode = models.CharField(max_length=50)
    Type = models.CharField(max_length=20)
    from_class = models.CharField(max_length=50)
    Communicating_facilities = models.CharField(max_length=250)
    Available_streams_after_10th = models.CharField(max_length=250)
    Type_of_board = models.CharField(max_length=50, null=True)
    Total_Students = models.CharField(max_length=50)
    safety_and_Securtiy_Measures = models.CharField(max_length=250)
    CCTV = models.CharField(max_length=50)
    students_per_teacher = models.CharField(max_length=50)
    Mention = models.CharField(max_length=50)
    Punishable_offence_include = models.CharField(max_length=100, null=True)
    Total_teachers = models.CharField(max_length=50)
    general_fee_structure = models.CharField(max_length=250)
    sports_played = models.CharField(max_length=50)
    Qualification_details_of_teachers = models.CharField(max_length=250)
    Facilities_provided = models.CharField(max_length=250)
    Major_achievements = models.CharField(max_length=150)
    Glorious_alumni_network = models.CharField(max_length=150)
    Teaching_ideology = models.CharField(max_length=150)
    Future_plans_and_developments = models.CharField(max_length=50)
    support_any_extra_activities_apart_from_curriculum = models.CharField(max_length=150)
    Principal_message = models.CharField(max_length=150)

    def __str__(self):
        return self.name_of_coaching