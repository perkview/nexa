from django.shortcuts import render
from .models import ContactMessage, BusinessChallenge

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    success = False
    error = False

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Basic validation
        if email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            success = True
        else:
            error = True

    return render(request, 'contact.html', {"success": success, "error": error})

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def submit_problem(request):
    success = False
    error = False

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        business_type = request.POST.get("business_type")
        company_size = request.POST.get("company_size")
        email = request.POST.get("email")
        problem = request.POST.get("problem")
        file_upload = request.FILES.get("file_upload")

        if email and problem and business_type and company_size:
            BusinessChallenge.objects.create(
                full_name=full_name,
                business_type=business_type,
                company_size=company_size,
                email=email,
                problem=problem,
                file_upload=file_upload
            )
            success = True
        else:
            error = True
    return render(request, 'submit_problem.html', {"success": success, "error": error})