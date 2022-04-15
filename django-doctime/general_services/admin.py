from django.contrib import admin

from general_services.models import (AppointMent,
            Medicine,
            MedicalTest,
            PescribedMedicine)

admin.site.register(AppointMent)
admin.site.register(Medicine)
admin.site.register(MedicalTest)
admin.site.register(PescribedMedicine)