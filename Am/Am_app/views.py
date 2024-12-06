import os

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from Am_app.models import Login ,Service_image, Residential,Building,Struturaldesign,Renovation,Swimming,Freelancing,Joinventure,Landscape,Fabrication,Paintcontract,Retro,Completed_project,Elevation,Dop,Certificate,Listofmachine,Gallery,JobApplication,EPF,ISO,LEI,MSME,ESIC,Oproject,Project,Contract,Contact,Ongoing,Completed
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib import messages


# Create your views here.
def index(request):
    images = Gallery.objects.all()# Fetch all service images from the database
    return render(request,'index.html',{'images':images})

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            udata = Login.objects.get(username=username)
            if password == udata.password:  # Use hashed password checks in production
                request.session['username'] = username
                request.session['utype'] = udata.utype

                if udata.utype == 'user':
                    return redirect('index')  # Redirect to a user-specific page
                else:
                    return redirect('admin_dashboard')  # Adjust as necessary
            else:
                messages.error(request, 'Invalid password')
        except Login.DoesNotExist:
            messages.error(request, 'Invalid Username')

    return render(request, 'login.html')





def admin_dashboard(request):
    return render(request,'admin_dshboard.html')


def service(request):
    return render(request,'service.html')


def upload_service_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Service_image(image=image, description=desc)
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Service_image.objects.all()  # Fetch all images to display on the page
    return render(request, 'service.html', {'success': success, 'images': images})


def service_view(request):
    services = Service_image.objects.all()  # Fetch all service images
    return render(request, 'service_view.html', {'services': services})


def service_view1(request):
    services = Service_image.objects.all()  # Fetch all service images
    return render(request, 'service_view1.html', {'services': services})

def elevation(request):
    return render(request,'elevation.html')

def upload_Elevation_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Residential(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Residential.objects.all()  # Fetch all images to display on the page
    return render(request, 'elevation.html', {'success': success, 'images': images})


def elevation_view(request):
    images = Residential.objects.all()  # Fetch all Residential objects
    return render(request, 'elevation_view.html', {'images': images})

def elevation_view1(request):
    images = Residential.objects.all()  # Fetch all Residential objects
    return render(request, 'elevation_view1.html', {'images': images})

def building(request):
    return render(request,'building.html')

def upload_building_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Building(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Building.objects.all()  # Fetch all images to display on the page
    return render(request, 'building.html', {'success': success, 'images': images})


def building_view(request):
    images = Building.objects.all()  # Fetch all Residential objects
    return render(request, 'building_view.html', {'images': images})

def building_view1(request):
    images = Building.objects.all()  # Fetch all Residential objects
    return render(request, 'building_view1.html', {'images': images})

@require_http_methods(["DELETE"])
def delete_building(request, image_id):
    try:
        image = Building.objects.get(id=image_id)
        image.delete()
        return JsonResponse({'success': True})
    except Building.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Image not found.'}, status=404)


def structural(request):
    return render(request,'structural.html')

def upload_structural_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Struturaldesign(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Struturaldesign.objects.all()  # Fetch all images to display on the page
    return render(request, 'structural.html', {'success': success, 'images': images})


def structural_view(request):
    images = Struturaldesign.objects.all()  # Fetch all Residential objects
    return render(request, 'structural_view.html', {'images': images})



def structural_view1(request):
    images = Struturaldesign.objects.all()  # Fetch all Residential objects
    return render(request, 'structural_view1.html', {'images': images})

@require_http_methods(["DELETE"])
def delete_strutural(request, image_id):
    try:
        # Debugging: Log the image ID to confirm it's being passed correctly
        print(f"Trying to delete image with ID: {image_id}")

        # Fetch the image from the database using the provided ID
        image = Struturaldesign.objects.get(id=image_id)

        # Debugging: Log the image to ensure it exists
        print(f"Found image: {image}")

        # Delete the image
        image.delete()

        # Return a successful response
        return JsonResponse({'success': True})

    except Struturaldesign.DoesNotExist:
        # Handle the case where the image doesn't exist
        print(f"Image with ID {image_id} not found.")
        return JsonResponse({'success': False, 'error': 'Image not found.'}, status=404)

    except Exception as e:
        # Handle any other exceptions
        print(f"Error: {e}")
        return JsonResponse({'success': False, 'error': str(e)}, status=500)




def renovation(request):
    return render(request,'renovation.html')

def upload_renovation_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Renovation(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Renovation.objects.all()  # Fetch all images to display on the page
    return render(request, 'renovation.html', {'success': success, 'images': images})


def renovation_view(request):
    images = Renovation.objects.all()  # Fetch all Residential objects
    return render(request, 'renovation_view.html', {'images': images})


def renovation_view1(request):
    images = Renovation.objects.all()  # Fetch all Residential objects
    return render(request, 'renovation_view1.html', {'images': images})


@require_http_methods(["DELETE"])
def delete_renovation(request, image_id):
    try:
        # Get the image object from the database using the image_id
        image = Renovation.objects.get(id=image_id)

        # Delete the image
        image.delete()

        # Return a JSON response indicating success
        return JsonResponse({'success': True})

    except Renovation.DoesNotExist:
        # If the image does not exist, return an error response
        return JsonResponse({'success': False, 'error': 'Image not found.'}, status=404)

    except Exception as e:
        # Handle any other exceptions and return an error message
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

def swimming(request):
    return render(request,'swimming.html')

def upload_swimming_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Swimming(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Swimming.objects.all()  # Fetch all images to display on the page
    return render(request, 'swimming.html', {'success': success, 'images': images})


def swimming_view(request):
    images = Swimming.objects.all()  # Fetch all Residential objects
    return render(request, 'swimming_view.html', {'images': images})


def swimming_view1(request):
    images = Swimming.objects.all()  # Fetch all Residential objects
    return render(request, 'swimming_view1.html', {'images': images})


@require_http_methods(["DELETE"])
def delete_swimming(request, image_id):
    try:
        # Find the image by ID
        image = Swimming.objects.get(id=image_id)

        # Delete the image from the database
        image.delete()

        # Return a success response
        return JsonResponse({'success': True})

    except Swimming.DoesNotExist:
        # Return an error response if the image doesn't exist
        return JsonResponse({'success': False, 'error': 'Image not found.'}, status=404)

    except Exception as e:
        # Handle any other errors
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

def freelancing(request):
    return render(request,'freelancing.html')

def upload_freelancing_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Freelancing(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Freelancing.objects.all()  # Fetch all images to display on the page
    return render(request, 'freelancing.html', {'success': success, 'images': images})


def freelancing_view(request):
    images = Freelancing.objects.all()  # Fetch all Residential objects
    return render(request, 'freelancing_view.html', {'images': images})


def freelancing_view1(request):
    images = Freelancing.objects.all()  # Fetch all Residential objects
    return render(request, 'freelancing_view1.html', {'images': images})

@csrf_exempt  # Temporarily exempt CSRF validation if you aren't using CSRF tokens in development
@require_http_methods(["DELETE"])
def delete_freelancing(request, image_id):
    try:
        # Find the image by ID
        image = Freelancing.objects.get(id=image_id)

        # Delete the image from the database
        image.delete()

        # Return a success response
        return JsonResponse({'success': True})

    except Freelancing.DoesNotExist:
        # Return an error response if the image doesn't exist
        return JsonResponse({'success': False, 'error': 'Image not found.'}, status=404)

    except Exception as e:
        # Handle any other errors
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def joinventure(request):
    return render(request,'joinventure.html')

def upload_joinventure_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Joinventure(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Joinventure.objects.all()  # Fetch all images to display on the page
    return render(request, 'joinventure.html', {'success': success, 'images': images})


def joinventure_view(request):
    images = Joinventure.objects.all()  # Fetch all Residential objects
    return render(request, 'joinventure_view.html', {'images': images})


def joinventure_view1(request):
    images = Joinventure.objects.all()  # Fetch all Residential objects
    return render(request, 'joinventure_view1.html', {'images': images})


def delete_join(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        try:
            image = Joinventure.objects.get(id=image_id)
            image.delete()  # Delete the image from the database
            # Optionally delete the file from the file system if needed
            image.image.delete(save=False)
            return JsonResponse({'success': True})
        except Joinventure.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Image not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


def landscape(request):
    return render(request,'landscape.html')

def upload_landscape_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Landscape(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Landscape.objects.all()  # Fetch all images to display on the page
    return render(request, 'landscape.html', {'success': success, 'images': images})


def landscape_view(request):
    images = Landscape.objects.all()  # Fetch all Residential objects
    return render(request, 'landscape_view.html', {'images': images})

def landscape_view1(request):
    images = Landscape.objects.all()  # Fetch all Residential objects
    return render(request, 'landscape_view1.html', {'images': images})


def delete_land(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        try:
            image = Landscape.objects.get(id=image_id)
            image.delete()  # Delete the image from the database
            # Optionally delete the file from the file system if needed
            image.image.delete(save=False)
            return JsonResponse({'success': True})
        except Joinventure.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Image not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


def fabrication(request):
    return render(request,'fabrication.html')

def upload_fabrication_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Fabrication(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Fabrication.objects.all()  # Fetch all images to display on the page
    return render(request, 'fabrication.html', {'success': success, 'images': images})


def fabrication_view(request):
    images = Fabrication.objects.all()  # Fetch all Residential objects
    return render(request, 'fabrication_view.html', {'images': images})



def fabrication_view1(request):
    images = Fabrication.objects.all()  # Fetch all Residential objects
    return render(request, 'fabrication_view1.html', {'images': images})


def delete_fab(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        try:
            image = Fabrication.objects.get(id=image_id)
            image.delete()  # Delete the image from the database
            # Optionally delete the file from the file system if needed
            image.image.delete(save=False)
            return JsonResponse({'success': True})
        except Joinventure.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Image not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


def paintcontract(request):
    return render(request,'paintcontract.html')

def upload_contract_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Contract(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Contract.objects.all()  # Fetch all images to display on the page
    return render(request, 'paintcontract.html', {'success': success, 'images': images})


def paintcontract_view(request):
    images = Contract.objects.all()  # Fetch all Residential objects
    return render(request, 'paintcontract_view.html', {'images': images})



def paintcontract_view1(request):
    images = Contract.objects.all()  # Fetch all Residential objects
    return render(request, 'paintcontract_view1.html', {'images': images})


def retro_fitting(request):
    return render(request,'retro_fitting.html')

def upload_paintcontract_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Retro(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Retro.objects.all()  # Fetch all images to display on the page
    return render(request, 'retro_fitting.html', {'success': success, 'images': images})


def retro_fitting_view(request):
    images = Retro.objects.all()  # Fetch all Residential objects
    return render(request, 'retro_fitting_view.html', {'images': images})


def retro_fitting_view1(request):
    images = Retro.objects.all()  # Fetch all Residential objects
    return render(request, 'retro_fitting_view1.html', {'images': images})

def delete_retro(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        try:
            image = Retro.objects.get(id=image_id)
            image.delete()  # Delete the image from the database
            # Optionally delete the file from the file system if needed
            image.image.delete(save=False)
            return JsonResponse({'success': True})
        except Joinventure.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Image not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


def completed_project(request):
    return render(request,'completed_project.html')




def upload_completed_project(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Completed(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Completed.objects.all()  # Fetch all images to display on the page
    return render(request, 'completed_project.html', {'success': success, 'images': images})




def completed_project_view(request):
    projects = Completed.objects.all()  # Fetch all Residential objects
    return render(request, 'completed_project_view.html', {'projects': projects})


def completed_project_view1(request):
    projects = Completed.objects.all()  # Fetch all Project objects
    return render(request, 'completed_project_view1.html', {'projects': projects})




@csrf_exempt
def delete_project(request):
    if request.method == "POST":
        # Get the project ID from the POST data
        project_id = request.POST.get('project_id')

        if project_id:
            try:
                # Retrieve the project object
                project = get_object_or_404(Completed, id=project_id)

                # Delete the project
                project.delete()

                # Respond with success
                return JsonResponse({"success": True})
            except Project.DoesNotExist:
                # If the project does not exist
                return JsonResponse({"success": False, "error": "Project not found."})
        else:
            # If no project ID was provided
            return JsonResponse({"success": False, "error": "No project ID provided."})
    else:
        return JsonResponse({"success": False, "error": "Invalid request method."})

def ongoing_project(request):
    return render(request,'ongoing_project.html')


def upload_ongoing_project(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Ongoing(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Ongoing.objects.all()  # Fetch all images to display on the page
    return render(request, 'ongoing_project.html', {'success': success, 'images': images})




def ongoing_project_view(request):
    projects = Ongoing.objects.all()  # Fetch all Residential objects
    return render(request, 'ongoing_project_view.html', {'projects': projects})

def ongoing_project_view1(request):
    projects = Ongoing.objects.all()  # Fetch all Residential objects
    return render(request, 'ongoing_project_view1.html', {'projects': projects})




def delete_oproject(request):
    # Ensure the request is a POST request
    if request.method == 'POST':
        # Get the project ID from the POST data
        project_id = request.POST.get('project_id')

        # Validate that project_id is not None
        if project_id is not None:
            try:
                # Try to fetch the project with the provided ID
                project = get_object_or_404(Ongoing, id=project_id)

                # Delete the project
                project.delete()

                # Return a success response
                return JsonResponse({'success': True})
            except Project.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Project not found.'})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid project ID.'})

    # If the request is not POST, return an error
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def upload_dop(request):
    if request.method == 'POST':
        pdf = request.FILES.get('pdf')
        description = request.POST.get('description', '')

        if pdf:
            # Save the uploaded file and description
            dop = Dop(pdf=pdf, description=description)
            dop.save()

            return redirect('dop')  # Redirect to a success page or another view

    return render(request, 'dop.html')

def dop(request):
    return render(request,'dop.html')


def dop_view1(request):
    dop_objects = Dop.objects.all()  # Retrieve all Dop records
    return render(request, 'dop_view1.html', {'dop_objects': dop_objects})

def dop_view(request):
    dop_objects = Dop.objects.all()  # Retrieve all Dop records
    return render(request, 'dop_view.html', {'dop_objects': dop_objects})


def certificate(request):
    return render(request,'certificate.html')



def upload_certificate(request):
    if request.method == 'POST':
        pdf = request.FILES.get('pdf')
        description = request.POST.get('description', '')

        if pdf:
            # Save the uploaded file and description
            dop = Certificate(pdf=pdf, description=description)
            dop.save()

            return redirect('certificate')  # Redirect to a success page or another view

    return render(request, 'certificate.html')


@require_http_methods(["DELETE"])
def delete_certificate(request, certificate_id):
    try:
        certificate = Certificate.objects.get(id=certificate_id)
        certificate.delete()
        return JsonResponse({'success': True})
    except Certificate.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Certificate not found.'}, status=404)

def certificate_view1(request):
    dop_objects = Certificate.objects.all()  # Retrieve all Certificate records
    return render(request, 'certificate_view1.html', {'dop_objects': dop_objects})

def certificate_view(request):
    dop_objects = Certificate.objects.all()  # Retrieve all Dop records
    return render(request, 'certificate_view.html', {'dop_objects': dop_objects})

def listofmachine(request):
    return render(request,'listofmachine.html')


def upload_listofmachine(request):
    if request.method == 'POST':
        pdf = request.FILES.get('pdf')
        description = request.POST.get('description', '')

        if pdf:
            # Save the uploaded file and description
            dop = Listofmachine(pdf=pdf, description=description)
            dop.save()

            return redirect('listofmachine')  # Redirect to a success page or another view

    return render(request, 'listofmachine.html')


def listofmachine_view1(request):
    dop_objects = Listofmachine.objects.all()  # Retrieve all Dop records
    return render(request, 'listofmachine_view1.html', {'dop_objects': dop_objects})

def listofmachine_view(request):
    dop_objects = Listofmachine.objects.all()  # Retrieve all Dop records
    return render(request, 'listofmachine_view.html', {'dop_objects': dop_objects})



def about(request): # Retrieve all Directos objects
    return render(request, 'about.html')



def gallery(request):
    return render(request,'gallery.html')

def upload_gallery_image(request):
    success = None
    if request.method == 'POST' and request.FILES:
        image_files = request.FILES.getlist('image')
        descriptions = request.POST.getlist('description')  # Get list of descriptions

        for image, desc in zip(image_files, descriptions):
            new_image = Gallery(image=image, description=desc)  # Corrected to use Residential
            new_image.save()

        success = 'Images uploaded successfully!'

    images = Gallery.objects.all()  # Fetch all images to display on the page
    return render(request, 'gallery.html', {'success': success, 'images': images})


def gallery_view(request):
    images = Gallery.objects.all()  # Fetch all Gallery objects
    return render(request, 'gallery_view.html', {'images': images})

def gallery_view1(request):
    images = Gallery.objects.all()  # Fetch all Residential objects
    return render(request, 'gallery_view1.html', {'images': images})


@require_http_methods(["DELETE"])
def delete_gallery(request, image_id):
    try:
        image = Gallery.objects.get(id=image_id)
        image.delete()
        return JsonResponse({'success': True})
    except Gallery.DoesNotExist:  # Corrected this to Gallery instead of Building
        return JsonResponse({'success': False, 'error': 'Image not found.'}, status=404)

from django.core.mail import send_mail
from django.core.mail import EmailMessage
import os

def job_application_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        resume = request.FILES.get('resume')  # Access the uploaded file here

        # Validate the file type
        if resume:
            ext = os.path.splitext(resume.name)[1].lower()
            allowed_extensions = ['.pdf', '.doc', '.docx']
            if ext not in allowed_extensions:
                return render(request, 'career.html', {
                    'error': 'Invalid file type. Only PDF and DOC files are allowed.'
                })

            # Create a new JobApplication instance and save it
            application = JobApplication(
                full_name=full_name,
                email=email,
                phone=phone,
                address=address,
                resume=resume  # This should now correctly save the file
            )
            application.save()

            # Send confirmation email with attachment
            subject = f"New Job Application for {resume}"
            message = f"""
            You have received a new job application!

            Full Name: {full_name}
            Email: {email}
            Phone: {phone}
            address: {address}
            """
            from_email = 'mahindrag154@gmail.com'  # Change this to the sender's email
            recipient_list = ['mahindrag154@gmail.com']  # Change this to the recipient's email

            email = EmailMessage(
                subject,
                message,
                from_email,
                recipient_list,
            )
            email.attach(resume.name, resume.read(), resume.content_type)

            try:
                email.send(fail_silently=False)
            except Exception as e:
                return render(request, 'career.html', {
                    'error': f"Error sending email: {e}"
                })

            return redirect('index')  # Redirect to a success page

    return render(request, 'career.html')



def epf(request):
    return render(request,'epf.html')



def upload_epf(request):
    if request.method == 'POST':
        pdf = request.FILES.get('pdf')
        description = request.POST.get('description', '')

        if pdf:
            # Save the uploaded file and description
            dop = EPF(pdf=pdf, description=description)
            dop.save()

            return redirect('epf')  # Redirect to a success page or another view

    return render(request, 'epf.html')


def epf_view1(request):
    dop_objects = EPF.objects.all()  # Retrieve all Dop records
    return render(request, 'epf_view1.html', {'dop_objects': dop_objects})

def epf_view(request):
    dop_objects = EPF.objects.all()  # Retrieve all Dop records
    return render(request, 'epf_view.html', {'dop_objects': dop_objects})




def iso(request):
    return render(request,'iso.html')



def upload_iso(request):
    if request.method == 'POST':
        pdf = request.FILES.get('pdf')
        description = request.POST.get('description', '')

        if pdf:
            # Save the uploaded file and description
            dop = ISO(pdf=pdf, description=description)
            dop.save()

            return redirect('iso')  # Redirect to a success page or another view

    return render(request, 'iso.html')


def iso_view1(request):
    dop_objects = ISO.objects.all()  # Retrieve all Dop records
    return render(request, 'iso_view1.html', {'dop_objects': dop_objects})

def iso_view(request):
    dop_objects = ISO.objects.all()  # Retrieve all Dop records
    return render(request, 'iso_view.html', {'dop_objects': dop_objects})





def lei(request):
    return render(request,'lei.html')


def upload_lei(request):
    if request.method == 'POST':
        pdf = request.FILES.get('pdf')
        description = request.POST.get('description', '')

        if pdf:
            # Save the uploaded file and description
            dop = LEI(pdf=pdf, description=description)
            dop.save()

            return redirect('lei')  # Redirect to a success page or another view

    return render(request, 'lei.html')


def lei_view1(request):
    dop_objects = LEI.objects.all()  # Retrieve all Dop records
    return render(request, 'lei_view1.html', {'dop_objects': dop_objects})

def lei_view(request):
    dop_objects = LEI.objects.all()  # Retrieve all Dop records
    return render(request, 'lei_view.html', {'dop_objects': dop_objects})


def msme(request):
    return render(request,'msme.html')


def upload_msme(request):
    if request.method == 'POST':
        pdf = request.FILES.get('pdf')
        description = request.POST.get('description', '')

        if pdf:
            # Save the uploaded file and description
            dop = MSME(pdf=pdf, description=description)
            dop.save()

            return redirect('msme')  # Redirect to a success page or another view

    return render(request, 'msme.html')


def msme_view1(request):
    dop_objects =MSME.objects.all()  # Retrieve all Dop records
    return render(request, 'msme_view1.html', {'dop_objects': dop_objects})

def msme_view(request):
    dop_objects = MSME.objects.all()  # Retrieve all Dop records
    return render(request, 'msme_view.html', {'dop_objects': dop_objects})





def esic(request):
    return render(request,'esic.html')


def upload_esic(request):
    if request.method == 'POST':
        pdf = request.FILES.get('pdf')
        description = request.POST.get('description', '')

        if pdf:
            # Save the uploaded file and description
            dop = ESIC(pdf=pdf, description=description)
            dop.save()

            return redirect('esic')  # Redirect to a success page or another view

    return render(request, 'esic.html')


def esic_view1(request):
    dop_objects =ESIC.objects.all()  # Retrieve all Dop records
    return render(request, 'esic_view1.html', {'dop_objects': dop_objects})

def esic_view(request):
    dop_objects = ESIC.objects.all()  # Retrieve all Dop records
    return render(request, 'esic_view.html', {'dop_objects': dop_objects})


def index(request):
    if request.method == 'POST':
        # Get data from the form
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create a new Contact instance and save it to the database
        contact_instance = Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            subject=subject,
            message=message,
        )
        contact_instance.save()

        # Send a confirmation email
        subject_email = "New Inquiry from Contact Form"
        email_message = f"""
        You have received a new inquiry!

        Full Name: {first_name} {last_name}
        Email: {email}
        Phone: {phone}
        Subject: {subject}
        Message: {message}
        """

        from_email = 'mahindrag154@gmail.com'  # Change this to the sender's email
        recipient_list = ['mahindrag154@gmail.com']  # Change this to the recipient's email

        email = EmailMessage(
            subject_email,
            email_message,
            from_email,
            recipient_list,
        )

        try:
            email.send(fail_silently=False)
        except Exception as e:
            return render(request, 'index.html', {
                'error': f"Error sending email: {e}"
            })

        return redirect('index')  # Redirect to the same page or a success page

    return render(request, 'index.html')
