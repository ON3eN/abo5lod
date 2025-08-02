from django.db import models

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='core/logo/', blank=True, null=True)
    maintenance_mode = models.BooleanField(default=False)

    def __str__(self):
        return self.site_name
