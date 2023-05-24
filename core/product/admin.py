from django.contrib import admin
from .models import UsersTable,MaterialsTable,CoursesTable,EnrollmentsTable,ProgressTable,MessageTable,CertificateTable,ProfilesTable
from django.db import models
from django.forms import TextInput
from django.forms import TextInput, Textarea

class UsersTableAdmin(admin.ModelAdmin):
    list_display = ('user_id','user_name','user_age','user_born_date','user_major','user_semester','user_email','username')
    list_display_links = ('user_id','user_name','user_age','user_born_date','user_major','user_semester','user_email','username')
    list_filter = ('user_major','user_semester')
    search_fields = ('user_name',)
    sortable_by = ('user_name',)
    ordering = ('user_id',)
    date_hierarchy = 'user_born_date'
    formfield_overrides = {
        models.CharField:{'widget': TextInput(attrs={'size': '10'})}
    }
    
    
class MaterialsTableAdmin(admin.ModelAdmin):
    list_display = ('materials_type','materials_title','materials_content')
    list_display_links = ('materials_type','materials_title','materials_content')
    list_filter = ('materials_type',)
    search_fields = ('materials_title',)
    sortable_by = ('materials_id',)
    ordering = ('materials_type',)
    
class CoursesTableAdmin(admin.ModelAdmin):
    list_display = ('courses_title','courses_description','courses_instructor','courses_duration','courses_prerequisities','courses_user_id')
    list_display_links = ('courses_title','courses_description','courses_instructor','courses_duration','courses_prerequisities','courses_user_id')
    list_filter = ('courses_instructor',)
    search_fields = ('courses_title',)

    
class EnrollmentsTableAdmin(admin.ModelAdmin):
    list_display = ('enrollment_id','payment_status','course_id')
    list_display_links = ('enrollment_id','payment_status','course_id')
    list_filter = ('course_id',)
    sortable_by = ('payment_status',)
    ordering = ('enrollment_id',)
    
class ProgressTableAdmin(admin.ModelAdmin):
    list_display = ('progress_id','lecture_complete','quiz_complete','assignment_complete','user_id','course_id')
    list_display_links = ('progress_id','lecture_complete','quiz_complete','assignment_complete','user_id','course_id')
    list_filter = ('lecture_complete',)
    search_fields = ('lecture_complete','quiz_complete')
    sortable_by = ('lecture_complete','quiz_complete')
    ordering = ('progress_id',)
    
class MessageTableAdmin(admin.ModelAdmin):
    list_display = ('message_content','message_user_id','message_courses_id')
    list_display_links = ('message_content','message_user_id','message_courses_id')
    list_filter = ('message_content',)
    search_fields = ('message_content',)
    sortable_by = ('message_content',)
    ordering = ('message_id',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})},
    }
    
class CertificateTableAdmin(admin.ModelAdmin):
    list_display = ('certificate_title','certificate_url','user_id','course_id')
    list_display_links = ('certificate_title','certificate_url','user_id','course_id')
    search_fields = ('certificate_title',)
    sortable_by = ('certificate_title',)
    ordering = ('certificate_id',)
    
class ProfilesTableAdmin(admin.ModelAdmin):
    list_display = ('profiles_title','user_id')
    list_display_links = ('profiles_title','user_id')
    list_filter = ('profiles_title',)
    search_fields = ('profiles_title',)
    sortable_by = ('profiles_id',)
    ordering = ('profiles_title',)
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})},
    }
    
admin.site.register(UsersTable,UsersTableAdmin)
admin.site.register(MaterialsTable,MaterialsTableAdmin)
admin.site.register(CoursesTable,CoursesTableAdmin)
admin.site.register(EnrollmentsTable,EnrollmentsTableAdmin)
admin.site.register(ProgressTable,ProgressTableAdmin)
admin.site.register(MessageTable,MessageTableAdmin)
admin.site.register(CertificateTable,CertificateTableAdmin)
admin.site.register(ProfilesTable,ProfilesTableAdmin)

