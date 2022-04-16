from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from users.models import Profile
from general_services.models import AppointMent, PescribedMedicine
from general_services.forms import PescribedMedicineForm
from general_services.utils import encrypt, decrypt

def doctor_list(request):
    context = {
        'doctors': Profile.objects.filter(user_type = 'doctor').all()
    }

    return render(request, 'doctor_list.html', context)

@login_required
def doctor_details(request, id):
    context = {
        'doctor': Profile.objects.get(pk=id)
    }

    return render(request, 'doctor_details.html', context)

@login_required
def book_appoinment(request, doctor_id):
    context = {}

    if request.method == 'POST':
        appoinment_time = request.POST.get('appoinment_date')
        contact_no = request.POST.get('contact_no') 
        age = request.POST.get('age')
        doctor = User.objects.get(pk=doctor_id)

        appoinment = AppointMent(
            doctor=doctor,
            patient=request.user,
            appointment_time=appoinment_time,
            contact_no=contact_no,
            age=age
        )
        appoinment.save()

        messages.success(request,"Appoinment Recieved Successfully")
        return redirect('home')

    return render(request, 'book_appoinment.html', context)


@login_required
def change_appoinment_status(request, id):
    appoinment = AppointMent.objects.get(pk=id)
    appoinment.appointment_status = not appoinment.appointment_status
    appoinment.save()
    print(f'Appoinment id is {appoinment.id}')
    return redirect('home')

@login_required
def add_pescription(request, id):
    context = {}
    if request.method == 'POST':
        pescription = PescribedMedicineForm(request.POST)
        pescription.instance.appointment = AppointMent.objects.get(pk=id)
        pescription.save()
        # instance = pescription.save(commit=False)        
        # instance.comments = encrypt(instance.comments)
        # instance.save()
        return redirect('home')
    else:
        context['form'] = PescribedMedicineForm()
    return render(request, 'add_pescription.html', context)

@login_required
def delete_appoinment(request, id):
    appointment = AppointMent.objects.get(pk=id)
    appointment.delete()
    return redirect('home')

@login_required
def patient_pescription(request, id):
    pescription = None
    try:
        pescription = PescribedMedicine.objects.get(
                    appointment=AppointMent.objects.get(pk=id)
                )
        pescription.comments = decrypt(pescription.comments)
    except:
        pass
    
    context = {
        'pescription': pescription
    }

    return render(request, 'patient_pescription.html', context)