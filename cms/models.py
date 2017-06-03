from django.db import models

# Create your models here.
# python3 manage.py makemigrations
# python3 manage.py migrate

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField()
    url = models.CharField(max_length=50)
    type = models.IntegerField()
    status = models.IntegerField()
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    remark = models.CharField(max_length=255)
    order = models.IntegerField()


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    pid = models.IntegerField()
    status = models.IntegerField()
    remark = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    order = models.IntegerField()

class RoleUser(models.Model):
    id = models.AutoField(primary_key=True)
    role_id = models.IntegerField()
    user_id = models.IntegerField()


