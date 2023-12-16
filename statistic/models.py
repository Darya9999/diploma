from django.db import models
from statistic.validators import validate_age
from statistic.validators import validate_bal
class Stat(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    sename = models.CharField(max_length=50, verbose_name="Фамилия")
    surname = models.CharField(max_length=50, verbose_name="Отчество")
    sud = models.BooleanField(verbose_name="Судимость", default=False)
    KINDS_OBR = (
        ('no', 'Нет'),
        ('prof', 'Профильное'),
        ('neprof', 'Непрофильное'),
    )
    kind_obr = models.CharField(max_length=6, choices=KINDS_OBR, blank=False, verbose_name="Образование", default='')
    KINDS_GRAD = (
        ('no', 'Нет'),
        ('prof', 'Профильное'),
        ('neprof', 'Непрофильное'),
    )
    age = models.IntegerField(verbose_name="Возраст", validators=[validate_age])
    KIND_EXP = (
        ('no', 'Нет'),
        ('prof1to3', 'Профильный от 1 до 3 лет'),
        ('profup3', 'Профильный от 3 лет'),
        ('neprof', 'Непрофильный опыт работы'),
    )
    kind_exp = models.CharField(max_length=8, choices=KIND_EXP, blank=False, verbose_name="Опыт работы", default='')
    exp_concurent = models.BooleanField(verbose_name="Опыт работы в компании-конкуренте", default=False)
    recomendacii = models.BooleanField(verbose_name="Наличие рекомендаций с прошлого места работы", default=False)
    profdop = models.BooleanField(verbose_name="Наличие профильного доп. образования", default=False)
    sredball = models.IntegerField(verbose_name="Средний балл диплома", validators=[validate_bal] )
    kollball = models.IntegerField(verbose_name="Итоговое количество баллов", null=True)
    class Meta:
        verbose_name_plural = 'Анкеты'
        verbose_name = 'Анкета'
        ordering = ['-kollball']

