from django.contrib import admin
from StudentApp.models import Students


# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    students_data = [Students.student_roll_number, Students.student_name, Students.student_class,
                     Students.student_address]


admin.site.register(Students, StudentsAdmin)
