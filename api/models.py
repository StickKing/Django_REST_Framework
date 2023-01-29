from django.db import models

#Кабинеты
class Office(models.Model):
    #Наменование
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

#Отдел, департамент
class Department(models.Model):
    #Наименование отдела
    name = models.CharField(max_length=100)
    #Телефон
    telefon = models.IntegerField()
    #Email группа рассылки 
    email = models.EmailField()
    #Создаю связь многие ко многим ы
    office = models.ManyToManyField(Office)

    def __str__(self):
        return f"{self.name}"

#Сотрудники    
class Person(models.Model):

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    #Имя
    first_name = models.CharField(max_length=50)
    #Фамилия
    second_name = models.CharField(max_length=50)
    #Отчество
    patronymic = models.CharField(max_length=50)
    #День рождения
    birthday = models.DateField()
    #Email
    email = models.EmailField()
    #Находится ли в отпуске
    in_vacation = models.BooleanField()

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.patronymic}"

class Post(models.Model):
    #Наименование 
    name = models.CharField(max_length=60)
    #
    salary = models.SmallIntegerField()
    person = models.ManyToManyField(Person)

    def __str__(self):
        return f"{self.name}"
