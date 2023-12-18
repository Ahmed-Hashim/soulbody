from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Categories)

admin.site.register(System_FQA)


class MedicalSystemsAdmin(admin.ModelAdmin):
    class Media:
        js = (
            "js/tinymce.min.js",
            "js/textEditor.js",
        )
        css = {"all": ("css/admin.css",)}


admin.site.register(MedicalSystem, MedicalSystemsAdmin)


class RequestClinicSystemPackageAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "phone_number",
        "email",
        "clinic_count",
        "departement_count",
        "doctors_count",
        "users_count",
        "details",
        "date",
    ]
    list_filter = [
        "name",
        "phone_number",
        "email",
        "clinic_count",
        "departement_count",
        "doctors_count",
        "users_count",
        "details",
        "date",
    ]


admin.site.register(RequestClinicSystemPackage, RequestClinicSystemPackageAdmin)


class RequestHospitalSystemPackageAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "name",
        "hosbital",
        "phone_number",
        "email",
        "hospital_beds_count",
        "departement_count",
        "doctors_count",
        "users_count",
        "details",
        "date",
    ]
    list_display = [
        "title",
        "name",
        "hosbital",
        "phone_number",
        "email",
        "hospital_beds_count",
        "departement_count",
        "doctors_count",
        "users_count",
        "details",
        "date",
    ]


admin.site.register(RequestHospitalSystemPackage, RequestHospitalSystemPackageAdmin)
