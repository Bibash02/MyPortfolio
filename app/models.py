from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ("uiux", "UI/UX Design Project"),
        ("django", "Django Project"),
        ("fullstack", "FullStack Project"),
        ("freelance", "Freelance Collaboration"),
        ("internship", "Internship"),
        ("hi", "Just saying hi"),
    ]

    BUDGET_CHOICES = [
        ("<10", "< $10"),
        ("10-20", "$10 – $20"),
        ("20-30", "$20 – $30"),
        ("30+", "$30+"),
        ("not_sure", "Not sure"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    budget = models.CharField(max_length=20, choices=BUDGET_CHOICES)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"
    