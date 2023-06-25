from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Element(models.Model):
    element = models.CharField('Элемент', max_length=50)
    name = models.CharField('Название', max_length=100)
    water_soluble = models.BooleanField('Водорастворимость')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'


class Plan(models.Model):
    name = models.CharField('Название', max_length=50)
    deadline = models.DateField('Срок', help_text='Введите дату в формате ГГГГ-ММ-ДД')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'План'
        verbose_name_plural = 'Планы'


class Wine(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name='План')
    photo = models.ImageField('Фото', upload_to='wine_photos')
    name = models.CharField('Название', max_length=100)
    quantity = models.PositiveIntegerField('Количество')

    class Meta:
        verbose_name = 'Вино'
        verbose_name_plural = 'Вина'


class Advice(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name='План', related_name='advices')
    text = models.TextField('Текст совета')

    def __str__(self):
        return f'{self.plan} - {self.text}'

    class Meta:
        verbose_name = 'Совет'
        verbose_name_plural = 'Советы'


class Risk(models.Model):
    RISK_CHOICES = (
        ('not_danger', 'Not Danger'),
        ('danger', 'Danger'),
        ('very_danger', 'Very Danger'),
    )
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name='План')
    description = models.TextField('Описание риска')
    risk_type = models.CharField('Тип риска', max_length=20, choices=RISK_CHOICES)

    class Meta:
        verbose_name = 'Риск'
        verbose_name_plural = 'Риски'


class Task(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name='План', related_name='tasks')
    number = models.IntegerField('Номер')
    name = models.CharField('Название', max_length=100)
    performer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='performed_tasks', verbose_name='Исполнитель')
    location = models.CharField('Расположение', max_length=100)
    responsible = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responsible_tasks', verbose_name='Ответственный')
    status = models.CharField('Статус', max_length=50)

    def __str__(self):
        return f'{self.plan.name} - {self.number} - {self.name}'

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
