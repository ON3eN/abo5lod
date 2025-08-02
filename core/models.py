from django.db import models

class SiteSetting(models.Model):
    site_name = models.CharField("اسم الموقع", max_length=100)
    logo = models.ImageField("شعار الموقع", upload_to='core/logo/', blank=True, null=True)
    maintenance_mode = models.BooleanField("وضع الصيانة", default=False)

    class Meta:
        verbose_name = "إعداد الموقع"
        verbose_name_plural = "إعدادات الموقع"

    def __str__(self):
        return self.site_name
