from django.db import models

# Create your models here.

class Mould(models.Model):
    number = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Mould number",
    )

    name = models.CharField(
        max_length=150,
        verbose_name="Mould name",
    )

    manufacture_year = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Manufacture year",
    )

    maker = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Mould maker",
    )

    owner = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Owner",
    )

    clamping_force = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Clamping force",
    )

    width = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Width, mm",
    )

    overall_width = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Overall width, mm",
    )

    length = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Length, mm",
    )

    overall_length = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="Overall length, mm",
    )

    height = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Height, mm",
    )

    moving_side_weight = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Moving side weight , kg",
    )

    fix_side_weight = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Fix side weight, kg",
    )

    total_weight = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Total weight, kg",
    )

    ejector = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Ejector",
    )

    unscrewing = models.BooleanField(
        default=False,
        verbose_name="Unscrewing",
    )

    hot_runner_nozzles = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Hot runner nozzles",
    )

    hot_runner_brand = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Hot runner brand",
    )

    pneumatic_core_fix_side = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Pneumatic core fix side",
    )

    pneumatic_core_moving_side = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Pneumatic core moving side",
    )

    hydraulic_core_fix_side = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Hydraulic core fix side",
    )

    hydraulic_core_moving_side = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Hydraulic core moving side",
    )

    servo_core_moving_side = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Servo core moving side",
    )

    imm_nozzle = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Imm nozzle",
    )

    cavities_total = models.PositiveSmallIntegerField(
        verbose_name="Total cavities",
    )

    cavities_active = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        verbose_name="Active cavities",
    )

    nominal_cycle_time = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Nominal cycle time, sec",
    )

    part_weight = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Part weight, g",
    )

    injection_weight = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Injection weight, g",
    )

    initial_closures = models.PositiveBigIntegerField(
        default=0,
        verbose_name="Initial closures",
    )

    total_closures = models.PositiveBigIntegerField(
        default=0,
        verbose_name="Total closures",
    )

    class Condition(models.TextChoices):
        GOOD = "good", "Good"
        BAD = "bad", "Bad"
        MIDDLE = "middle", "Middle"

    condition = models.CharField(
        max_length=30,
        choices=Condition.choices,
        default=Condition.GOOD,
        verbose_name="Condition",
    )

    comments = models.TextField(
        blank=True,
        verbose_name="Comments",
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(cavities_total__gt=0),
                name="mould_cavities_total_positive",
            ),
            models.CheckConstraint(
                condition=models.Q(cavities_active__isnull=True) 
                | models.Q(cavities_active__lte=models.F("cavities_total")),
                name="mould_active_cavities_lte_total",
            ),

            models.CheckConstraint(
                condition=models.Q(
                    total_closures__gte=models.F("initial_closures")
                ),
                name="mould_total_closures_gte_initial",
            ),
        ]
        
         
    def save(self, *args, **kwargs):
        if self._state.adding:
            self.total_closures = self.initial_closures
        super().save(*args, **kwargs)

