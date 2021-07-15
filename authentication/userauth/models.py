import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class customUseraDetails(AbstractUser):
    """Custom User Model where id and contactNumber is included"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contactNumber = models.CharField(max_length=15)
