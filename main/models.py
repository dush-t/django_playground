from django.db import models

# Create your models here.
class TestModel(models.Model):
    field1 = models.CharField(max_length=20, blank=True, null=True)
    field2 = models.IntegerField(default=0)
    field3 = models.BooleanField(default=True)
    version = models.PositiveIntegerField(default=1)

    def save(self, version=None):
        
        print(self.version)

        if self.version != version:
            return
            # pass
            
        self.version = self.version + 1
        return super().save()
        