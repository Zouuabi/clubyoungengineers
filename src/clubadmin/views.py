from django.shortcuts import redirect, render
from .models import Child, Programme, Group
from .forms import ProgrammeForm, GroupForm, ChildForm


def programmes (request): 
    programmes = Programme.objects.all()
    context = {
        "programmes":programmes
    }
    return render(request,"programmes.html", context)

def add_programme(request):
    if request.method == 'POST':
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(programmes)
            
    else:
        form = ProgrammeForm()
    
    return render(request, 'add_programme.html', {'form': form})



def groupes(request):
    groups = Group.objects.all()
    return render(request, 'groupes.html', {'groups': groups})


def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groupes')
    else:
        form = GroupForm()
    return render(request, 'add_group.html', {'form': form})

def modify_group(request, group_id):
    group = get_object(Group, id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('groups_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'modify_group.html', {'form': form})

def delete_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    group.delete()
    return redirect('groups_list')

def add_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(children_list)
    else:
        form = ChildForm()
    return render(request, 'add-child.html', {'form': form})

# def index (request):
#     return render(request,"index.html")
def children_list(request):
    children = Child.objects.all()
    return render(request, 'enfants.html', {'children': children})


def presences(request):
    return render(request, 'presences.html')

def paiements(request):
    return render(request, 'paiements.html')
