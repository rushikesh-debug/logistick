from django.db import models

class Parcel(models.Model):
    tracking_id = models.CharField(max_length=50)
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=150)
    delivery_location = models.CharField(max_length=150)
    weight = models.FloatField()
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tracking_id