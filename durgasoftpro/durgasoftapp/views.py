from django.shortcuts import render
from .models import ServicesData,FeedbackData,EnquiryData
from .forms import FeedbackForm,EnquiryForm
from django.http.response import HttpResponse
import  datetime as dt
date1=dt.datetime.now()

# Create your views here.
def home_view(request):
    return render(request,'durgasoft_home.html')

def services_view(request):
    services= ServicesData.objects.all()
    return render(request,'durgasoft_services.html',{'services':services})

def enquiry_view(request):
    if request.method=="POST":
        eform=EnquiryForm(request.POST)
        if eform.is_valid():
            name=request.POST.get('name')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            gender=request.POST.get('gender')
            courses=eform.cleaned_data.get('courses')
            shifts=eform.cleaned_data.get('shifts')
            start_date=eform.cleaned_data.get('start_date')
            data=EnquiryData(
                name=name,
                mobile=mobile,
                email=email,
                gender=gender,
                courses=courses,
                shifts=shifts,
                start_date=start_date
                )
            data.save()
            eform=EnquiryForm
            return render(request,'durgasoft_contact.html',{'eform':eform})
        else:
            return HttpResponse("User Invalid Data")
    else:
        eform=EnquiryForm()
        return render(request,'durgasoft_contact.html',{'eform':eform})

def gallery_view(request):
    return render(request,'durgasoft_gallery.html')

def feedback_view(request):
    if request.method=="POST":
       fform =FeedbackForm(request.POST)
       if fform.is_valid():
           name=request.POST.get('name')
           rating=request.POST.get('rating')
           feedback=request.POST.get('feedback')

           data=FeedbackData(
               name=name,
               rating=rating,
               feedback=feedback,
               date=date1
           )
           data.save()
           fform=FeedbackForm()
           fdata = FeedbackData.objects.all()
           return render(request,'durgasoft_feedback.html',{'feedbacks':fdata,'fform':fform})
       else:
           return HttpResponse(" User Invalid Data")

    else:
        feedbacks=FeedbackData.objects.all()
        fform=FeedbackForm()
        return render(request,'durgasoft_feedback.html',{'fform':fform,'feedbacks':feedbacks})