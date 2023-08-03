from django.db import models

class PaperType(models.TextChoices):
    Essay = "Essay", "Essay (Any Type)"
    AdmissionEssay = "AdmissionEssay", "Addmission Essay"
    AnnotatedBibliography = "AnnotatedBibliography", "Annotated Bibliography"
    ArgumentativeEssay = "ArgumentativeEssay", "Argumentative Essay"
    