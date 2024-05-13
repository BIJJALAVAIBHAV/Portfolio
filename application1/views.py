from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render,HttpResponse
from application1.models import FeedbackForm
# Create your views here.
def home(request):
    context = {'name':'Vaibhav','course':'Django','tutor':'Code with Harry'}
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')
    
def project(request):
    return render(request,'project.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        feedback = request.POST['Feedback']

        new_record = FeedbackForm(name=name,email=email,phone_number=phone,Feedback=feedback)
        new_record.save()
    return render(request,'contact.html',{})

def queries(request):
    feedbacks = FeedbackForm.objects.all()
    context = {
        'feedbacks':feedbacks
    }
    return render(request, 'feedbacks.html', context)

def login(request):
    return render(request,'login.html')

def viewdata(request, id):
    # Retrieve the feedback object with the provided id from the database
    feedback = get_object_or_404(FeedbackForm, id=id)
    
    # Pass the feedback object to the template for rendering
    return render(request, 'feedbacks.html', {"feedback": feedback})