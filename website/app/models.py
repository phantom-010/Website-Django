from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Contract(models.Model):
    contract_number = models.CharField(max_length=100, verbose_name="Номер договора")
    contract_date = models.DateField(verbose_name="Дата заключения")
    partner = models.CharField(max_length=255, verbose_name="Контрагент")
    subject = models.TextField(verbose_name="Предмет договора")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Договор №{self.contract_number} от {self.contract_date}"

class Taskadd(models.Model):
    title = models.CharField(max_length=100, verbose_name="Тема задачи")
    deadline = models.DateField(verbose_name="Срок выполнения")
    description = models.CharField(max_length=255, verbose_name="Описание")
    priority = models.TextField(verbose_name="Приоритет")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Договор №{self.title} от {self.deadline}"
 


     