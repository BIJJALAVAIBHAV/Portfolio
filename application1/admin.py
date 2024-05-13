from django.contrib import admin

from application1.models import FeedbackForm

class FeedbackForm_Admin(admin.ModelAdmin):
    list_display = ['id','name','email','phone_number','Feedback']
admin.site.register(FeedbackForm,FeedbackForm_Admin)    
