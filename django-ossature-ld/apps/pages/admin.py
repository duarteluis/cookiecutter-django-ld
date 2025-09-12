from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import FaqQuestionAnswer


@admin.register(FaqQuestionAnswer)
class FaqQuestionAnswerAdmin(admin.ModelAdmin):
    pass
