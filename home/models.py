from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class BusinessChallenge(models.Model):
    BUSINESS_TYPES = [
        ("Retail", "Retail"),
        ("Service", "Service"),
        ("Tech Startup", "Tech Startup"),
        ("Manufacturing", "Manufacturing"),
        ("Other", "Other"),
    ]

    COMPANY_SIZES = [
        ("Freelancer / Solo", "Freelancer / Solo"),
        ("Small Team (2-10)", "Small Team (2-10)"),
        ("Medium (11-50)", "Medium (11-50)"),
        ("Large (51+)", "Large (51+)"),
    ]

    full_name = models.CharField(max_length=200, blank=True, null=True)
    business_type = models.CharField(max_length=50, choices=BUSINESS_TYPES)
    company_size = models.CharField(max_length=50, choices=COMPANY_SIZES)
    email = models.EmailField()
    problem = models.TextField()
    file_upload = models.FileField(upload_to="uploads/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.business_type}"