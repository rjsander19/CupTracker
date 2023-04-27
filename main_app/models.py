from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

STATUS = (
    ('C', 'Clean'),
    ('D', 'Dirty')
)


class Content(models.Model):
    name = models.CharField(max_length=50)
    temp = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.temp} {self.name}'

    def get_absolute_url(self):
        return reverse('contents_detail', kwargs={'pk': self.id})


class Cup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    # age = models.IntegerField()
    contents = models.ManyToManyField(Content)

    def __str__(self):
        return f'the cups name is {self.name}'

    def get_absolute_url(self):
        return reverse('detail', kwargs = { 'cup_id': self.id })
    user = models.ForeignKey(User, on_delete=models.CASCADE) 


class Use(models.Model):
  date = models.DateField('use date')
  status = models.CharField(
    max_length=1,
    choices=STATUS,
    default=STATUS[0][0]
  )

  
  cup = models.ForeignKey(Cup, on_delete=models.CASCADE)

def __str__(self):
    return f"{self.get_status_display()} on {self.date}"

class Meta:
    ordering = ['-date']


