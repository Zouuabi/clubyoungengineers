from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello , Sarroura ! ")





def dashboard(request):
    # Sample data (you will fetch real data from the database)
    groupes = ['Group 1', 'Group 2', 'Group 3']
    enfants = ['Child 1', 'Child 2', 'Child 3']
    presences = ['Present', 'Absent', 'Present']
    paiements = ['Paid', 'Unpaid', 'Paid']
    
    context = {
        'groupes': groupes,
        'enfants': enfants,
        'presences': presences,
        'paiements': paiements
    }
    return render(request, 'index.html', context)

