from django.db import models

# Create your models here.
class Csv(models.Model):
    file_name = models.FileField(upload_to='upload_csv')
    uploaded = models.DateTimeField(auto_now_add=True)
    #balance = models.DecimalField(max_digits=5, decimal_places=2)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id : {self.id}"