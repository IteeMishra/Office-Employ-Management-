from django.contrib import admin

# Register your models here.
#by doing this we can access these table from admin access like we can add data from there itself and add data also superuser k through
from .models import Employee,Department,Role

admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)