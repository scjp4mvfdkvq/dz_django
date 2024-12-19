import datetime


from django.db import models


class Operation(models.Model):

    name = models.TextField(
        verbose_name="Наименование операции",
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание операции",
    )

    cost = models.FloatField(
        verbose_name="Стоимость",
    )

    operation_at = models.DateTimeField(
        default=datetime.datetime.now(),
        verbose_name="Дата операции",
    )

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"

    def __str__(self):
        return f"{self.name}"


class GoalType(models.TextChoices):
    """Тип цели"""

    SPENDING = "Трата"
    REFILL = "Пополнение"


class Goal(models.Model):
    """Модель цели траты или пополнения"""

    name = models.CharField(
        max_length=255,
        verbose_name="Название цели",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
    )
    goal_type = models.CharField(
        choices=GoalType.choices,
        default=GoalType.SPENDING,
        max_length=32,
        verbose_name="Тип операций цели",
    )
    start_date = models.DateField(
        default=datetime.date.today,
        verbose_name="Дата начала цели",
    )
    finish_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата окончания цели",
    )
    value = models.FloatField(
        verbose_name="Значение цели",
    )

    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"

class GoalManager(models.Manager):
    def goals(self):
        return self.filter(goal_type=GoalType.REFILL)

    def budgets(self):
        return self.filter(goal_type=GoalType.SPENDING)
