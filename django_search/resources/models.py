from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()
    
    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'
        
    def __str__(self) -> str:
        return self.name
    
    # def runspider(self):
        
        