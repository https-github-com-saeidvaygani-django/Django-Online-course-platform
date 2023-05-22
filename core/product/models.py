from django.db import models
from django.contrib.auth.models import User

class UsersTable(models.Model):
    user_id = models.AutoField(primary_key=True, verbose_name="Users Id")
    user_name = models.CharField(max_length=50, verbose_name="Name")
    user_age = models.IntegerField(max_length=2, verbose_name="Age")
    user_born_date = models.DateField(auto_created=now, verbose_name="Born")
    user_major = models.CharField(max_length=50, verbose_name="Major")
    user_semester = models.IntegerField(max_length=2, verbose_name="Semester")
    user_Email = models.EmailField(max_length=50, verbose_name="Email")
    username = models.CharField(User, max_length=50, verbose_name="User Name")
    password = models.CharField(max_length=8, verbose_name="Password")
    
    def __str__(self):
        return self.user_name
    
class MaterialsTable(models.Model):
    materials_id = models.AutoField(primary_key=True, verbose_name="Id")
    set_choice = (
        ('Video Lecture','Video Lecture'),
        ('Reading','Reading'),
        ('Writing','Writing'),
        ('Github Source','Github Source')
    )
    materials_type = models.CharField(max_length=50, choices=set_choice, null=True, verbose_name="Materials")
    materials_title = models.CharField(max_length=50, verbose_name="Title")
    materials_content = models.CharField(max_length=100, verbose_name="Contents")
    
    def __str__(self):
        return self.materials_id
    
class CoursesTable(models.Model):
    courses_id  = models.AutoField(primary_key=True, verbose_name="Course Id")
    courses_title = models.CharField(max_length=50, verbose_name="Course Title")
    course_description = models.TextField(max_length=200, verbose_name="Description")
    course_instructor = models.CharField(max_length=50, verbose_name="Instructor")
    course_duration = models.IntegerField(max_length=3, verbose_name="Duration")
    course_prerequisities = models.CharField(max_length=10, verbose_name="Course Prerequisities")
    course_user_id = models.ForeignKey('UsersTable', on_delete=models.CASCADE, verbose_name="User Id")
    
    def __str__(self):
        return self.course_title
    
class EnrollmentsTable(models.Model):
    enrollment_id = models.AutoField(primary_key=True, verbose_name="Enrollment Id")
    payment_status = models.BooleanField(default=False, verbose_name="Status")
    user_id = models.ManyToManyField('UsersTable', null=True, default='', verbose_name="User Id")
    course_id = models.ForeignKey('CoursesTable', on_delete=models.CASCADE, null=True, verbose_name="Course Id")
    
    def __str__(self):
        return self.enrollment_id
    
class ProgressTable(models.Model):
    progress_id = models.AutoField(primary_key=True, verbose_name="Id")
    lecture_complete = models.IntegerField(max_length=3, verbose_name="Lecture Complete")
    quiz_complete = models.IntegerField(max_length=3, verbose_name="Quiz Completed")
    assignment_complete = models.IntegerField(max_length=3, verbose_name="Assignment Complete")
    user_id = models.ForeignKey('UserTable', on_delete=models.CASCASE, verbose_name="User Id", null=True, default='')
    course_id = models.ForeignKey('CoursesTable', on_delete=models.CASCADE, verbose_name="Course Id", null=True, default='')
    
    def __str__(self):
        return self.lecture_complete
    
class MessageTable(models.Model):
    message_id = models.AutoField(primary_key=True, verbose_name="Message Id")
    message_content = models.TextField(max_length=100, verbose_name="Message Content")
    message_user_id = models.ForeignKey('UsersTable', verbose_name="User Id")
    message_courses_id = models.ForeignKey('CoursesTable', verbose_name="Courses Id")
    
    def __str__(self):
        return self.message_content
    
    
class CertificateTable(models.Model):
    certificate_id = models.AutoField(primary_key=True, verbose_name="Certificate Id")
    certificate_title = models.CharField(max_length=100, verbose_name="Certificate Title")
    certificate_url = models.CharField(max_length=100, verbose_name="Certificate Url")
    user_id = models.ForeignKey('UsersTable', verbose_name="User Id", on_delete=models.CASCADE, null=True, default='')
    course_id = models.ForeignKey('CoursesTable', on_delete=models.CASCADE, verbose_name="Course Id", null=True, default='')
    
    def __str__(self):
        return self.certificate_title
    
class ProfilesTable(models.Model):
    profiles_id = models.AutoField(primary_key=True, verbose_name="Profiles Id")
    profiles_title = models.TextField(max_length=100, verbose_name="Profiles Title")
    user_id = models.ForeignKey('UsersTable', verbose_name="User Id")
    
    def __str__(self):
        return self.profiles_title