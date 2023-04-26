from django.db import models
from django.urls import reverse

STATUS = (
    ('C', 'Clean'),
    ('D', 'Dirty')
)

# Create your models here.
class Cup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    # age = models.IntegerField()

    def __str__(self):
        return f'the cups name is {self.name}'

    def get_absolute_url(self):
        return reverse('detail', kwargs = { 'cup_id': self.id })


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


