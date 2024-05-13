from django.db import models

class FeedbackForm(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20,unique=True)
    Feedback = models.CharField(max_length=300,blank=False)

class card_skills(models.Model):
    pass

