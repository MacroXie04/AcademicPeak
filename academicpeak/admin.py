from django.contrib import admin
# Register your models here.

class UniversityAdmin(admin.ModelAdmin):
    list_display = (
        'university_rank', 'university_name', 'university_country', 'university_global_score', 'university_enrollment',
        'university_link', 'university_photo_link')
