from django.contrib import admin

from students.models import Student, TakeModule


# NOT to be confused with admin.register
admin.site.register(Student)
admin.site.register(TakeModule)
