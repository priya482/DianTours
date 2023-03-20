from django.db import models

# Create your models here.
class Packages(models.Model):
    pkg_id=models.IntegerField()
    pkg_type=models.CharField(max_length=10)
    pkg_title=models.CharField(max_length=10)
    dep_date=models.DateField()
    pkg_from=models.CharField(max_length=10)
    pkg_to=models.CharField(max_length=10)
   # pkg_pic=models.ImageField()
    pkg_dec=models.CharField(max_length=100)
    pkg_price=models.IntegerField()
    pkg_days=models.IntegerField()
    pkg_night=models.IntegerField()
    tota_seats=models.IntegerField()
    avil_seats=models.IntegerField()
    pkg_status=models.BooleanField(default=True)

    class Meta:
        ordering = ['-pkg_id']

    def __str__(self):
        return self.pkg_title
