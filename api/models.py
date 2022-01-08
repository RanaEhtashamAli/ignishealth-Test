from django.db import models

# Create your models here.
class Data(models.Model):
    date = models.DateField()
    channel = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    os = models.CharField(max_length=25)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Data'

    def __str__(self):
        return f"{self.channel} {self.country}"


