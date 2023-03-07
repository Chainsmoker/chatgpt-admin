from django.db import models

# Create your models here.
class BlackListUsers(models.Model):
    number = models.CharField(max_length=255, unique=True)
    reason = models.TextField()

    def __str__(self) -> str:
        return self.number
    
    class Meta:
        verbose_name = "Black List User"
        verbose_name_plural = "Black List Users"