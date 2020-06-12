from django.db import models

class User(models.Model):
    name=models.CharField(max_length=128,unique=True)
    password=models.CharField(max_length=256)
    email=models.EmailField(unique=True)
    created_time=models.DateTimeField(auto_now_add=True)
    has_confirmed=models.BooleanField(default=False)
    authority=models.CharField(max_length=10,default='user')
    regions=models.ManyToManyField('Region',blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-created_time']
        verbose_name='用户'
        verbose_name_plural='用户'

class ConfirmString(models.Model):
    code=models.CharField(max_length=256)
    user=models.OneToOneField('User',on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name+": "+self.code

    class Meta:
        ordering=['-created_time']
        verbose_name='确认码'
        verbose_name_plural='确认码'

class Region(models.Model):
    name=models.CharField(max_length=64)
    adcode=models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['adcode']
        verbose_name='地区'
        verbose_name_plural='地区'