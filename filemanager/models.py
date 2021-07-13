from django.db import models

class ApplicationFile(models.Model):
    filename = models.CharField(max_length= 100)
    file_size = models.DecimalField(max_digits= 9, decimal_places= 0)
    upload_date = models.DateTimeField(auto_now_add= True)
    file_content = models.TextField()

    def __str__(self):
        return self.filename
