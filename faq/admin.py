from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("__str__", "language_code")
    search_fields = ("question", "question_hi", "question_bn")
    list_filter = ("language_code",)
    fieldsets = (
        (None, {"fields": ("question", "answer")}),
        (
            "Translations",
            {
                "fields": ("question_hi", "answer_hi", "question_bn", "answer_bn"),
                "classes": ("collapse",),
                "description": "Auto-generated translations. You may edit them manually if necessary.",
            },
        ),
    )
