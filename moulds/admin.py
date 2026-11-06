
from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Mould


@admin.register(Mould)
class MouldAdmin(ModelAdmin):
    list_display = (
        "number",
        "name",
        "maker",
        "cavities_total",
        "cavities_active",
        "condition",
        "total_closures",
    )

    search_fields = (
        "number",
        "name",
        "maker",
        "owner",
    )

    list_filter = (
        "condition",
        "maker",
    )

    readonly_fields = (
        "total_closures",
    )

    
    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return ("initial_closures", "total_closures")

        return ("total_closures",)


    
    fieldsets = (
        (
            "General Information",
            {
                 "classes": ["tab"],
                 "fields": (
                     "number",
                     "name",
                     "manufacture_year",
                     "maker",
                     "owner",
                ),
            },
        ),
        (
            "Dimensions and Weight",
             {
                "classes": ["tab"],
                "fields": (
                    "clamping_force",
                    ("width", "overall_width"),
                    ("length", "overall_length"),
                    "height",
                    ("moving_side_weight", "fix_side_weight"),
                    "total_weight",
                ),
            },
        ),
        (
            "Construction",
            {   "classes": ["tab"],
                "fields": (
                    ("ejector", "unscrewing"),
                    ("hot_runner_nozzles", "hot_runner_brand"),
                    (
                        "pneumatic_core_fix_side",
                        "pneumatic_core_moving_side",
                    ),
                    (
                        "hydraulic_core_fix_side",
                        "hydraulic_core_moving_side",
                    ),
                    ("servo_core_moving_side", "imm_nozzle"),
                ),
            },
        ),
        (
            "Production Parameters",
            {
                "classes": ["tab"],
                "fields": (
                    "cavities_total",
                    "cavities_active",
                    "nominal_cycle_time",
                    "part_weight",
                    "injection_weight",
                ),
            },
        ),
        (
            "Counters and Condition",
            {   "classes": ["tab"],
                "fields": (
                    "initial_closures",
                    "total_closures",
                    "condition",
                    "comments",
                ),
            },
        ),
    )

