from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Lead,Agent
from .forms import LeadForm,LeadModelForm


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
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html",context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html",context)


def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")

# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         print('Receiving a post request')
#         if form.is_valid():
#             print('the form is valid')
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.object.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent
#             )
#             return redirect("/leads")
#             print("")
#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html",context)