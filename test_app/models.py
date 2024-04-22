from django.db import models

# Create your models here.
from django.utils import timezone
from datetime import date

class Test(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    serial = models.IntegerField(null=True,blank=True,editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            today = timezone.now().date()
            print(today)
            last_instance = Test.objects.filter(date__date=today).order_by('-serial').first()

            if last_instance:
                if last_instance.date.date() != date.today():
                    print('in')
                    self.serial = 1
                else:
                    self.serial = last_instance.serial + 1
            else:
                print('out')
                self.serial = 1

        super(Test, self).save(*args, **kwargs)

    # class Meta:
    #     app_label = 'test_app'
        



class Guard(models.Model):
    name = models.CharField(max_length=20)

    