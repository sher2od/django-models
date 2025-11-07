from django.db import models

class Task(models.Model):
    PRIOTRY_CHOICES = [
        ['1','muxim'],
        ['2','sal muxim'],
        ['3','qilmasa ham boladi'],
        ['4','asosiy']
    ]
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True,null=True,default="")
    priorty = models.CharField(
        choices=PRIOTRY_CHOICES,
        default='4'
    )
    

    def __str__(self):
        return f'Task(id={self.id},name="{self.name}")'
    
