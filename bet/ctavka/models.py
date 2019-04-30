from django.db import models


class Ctavka(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True) #поле можно не заполнять
    price = models.FloatField(null=True, blank=True)
    coefficient = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    sport = models.ForeignKey("Sport", null=True, on_delete=models.PROTECT, verbose_name='спорт')
    total = models.ForeignKey("Total", null=True, on_delete=models.PROTECT, verbose_name='итог ставки')

    class Meta:
        verbose_name_plural = "Ставки"
        verbose_name = 'Ставка'
        ordering = ['-published']




#Модель отвечает за выбор спорта
class Sport(models.Model):
    sport_name = models.CharField(max_length=30, verbose_name='Вид спорта')

    def __str__(self):
        return self.sport_name

    class Meta:
        verbose_name_plural = "Выбор спорта"
        verbose_name = "Выбор спорта"
        ordering = ["sport_name"]


class Total(models.Model):
    total = models.CharField(max_length=30, verbose_name='Итоги события')

    def __str__(self):
        return self.total

    class Meta:
        verbose_name_plural = "Итоги"
        verbose_name = "Итог"
        ordering = ["total"]
