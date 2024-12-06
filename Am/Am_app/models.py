from django.db import models

# Create your models here.



class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    utype=models.CharField(max_length=50)

class Service_image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"



class Residential(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"


class Building(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Struturaldesign(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Elevation(models.Model):
    image = models.ImageField(upload_to='elevations/')  # This field must exist
    description = models.TextField()

    def __str__(self):
        return self.description


class Renovation(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"


class Swimming(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Freelancing(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Joinventure(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Landscape(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Fabrication(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Paintcontract(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"


class Contract(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Retro(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Detailed(models.Model):
    image = models.ImageField(upload_to='uploads/')
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Completed_project(models.Model):
    title = models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')

class Ongoing_project(models.Model):
    title = models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')

class Dop(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"


class Certificate(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"


class Listofmachine(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Gallery(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"


class JobApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.full_name



class EPF(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"



class ISO(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"



class LEI(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"



class MSME(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"


class ESIC(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"


class Oproject(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"


class Project(models.Model):
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.EmailField(unique=True)
    email = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=15)
    message = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name

class Ongoing(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"

class Completed(models.Model):
    image = models.ImageField(upload_to='uploads/')
    description = models.TextField(blank=True, null=True)  # New field for the description

    def __str__(self):
        return self.description or "No Description"