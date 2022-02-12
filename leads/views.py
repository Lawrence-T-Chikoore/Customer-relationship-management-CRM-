from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead,Agent
from .forms import LeadForm


def lead_list(request):
    leads = Lead.objects.all()
    context={
        "leads":leads
    }
    return render(request,"leads/leads_list.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead":lead
    }
    return render(request, "leads/lead_deatails.html",context)

def lead_create(request):
    form = LeadForm()
    if request.method == "POST":
        print('Receiving a post request')
        if form.is_valid():
            print('the form is valid')
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.object.create(
                first_name = first_name,
                last_name = last_name,
                age = age,
                agent = agent
            )
            print("")
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html",context)
