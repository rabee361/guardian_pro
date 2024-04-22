from django.db import models
from uuid import uuid4
from django.contrib.auth import get_user_model

# class Message(models.Model):
#     DEVICE_COICES = (
#         ('android','android'),
#         ('ios','ios'),
#         ('web','web')
#     )
#     device_id = models.CharField(max_length=200)
#     question = models.CharField(max_length=200)
#     answer = models.CharField(max_length=200)
#     device_type = models.CharField(max_length=20)


#     def save(self,obj):
#         pass


#     def __str__(self):
#         return self.device_id

User = get_user_model()



class Chat(models.Model):
    members = models.ManyToManyField(User)

    def add_user(self,request, user):
        self.members.add(user)
        self.save()
        return

    def __str__(self):
        return f'{self.id}'



class Employee(models.Model):
    name = models.CharField(max_length=100)





class Message(models.Model):
    sender = models.ForeignKey(User , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=100)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE,null=True)
    employee = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'




class Soura(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Image(models.Model):
    soura = models.ForeignKey(Soura,on_delete=models.CASCADE, null=True)
    # page = 
    image = models.ImageField(upload_to='images/souras/')

    def __str__(self):
        return f'{self.soura.name}-{self.id}'



