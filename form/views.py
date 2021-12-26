from django.shortcuts import render, redirect
from form.forms import PersonForm, PersonModelForm


# Create your views here.
def form_test(request):
    person_form = PersonModelForm()
    return render(request, 'form.html', {'form': person_form})

# def form_test(request):
#    if request.method == 'POST':
#        print(request.POST)
#        data = PersonForm(request.POST)
#        if data.is_valid():
#            data.save()
#            return redirect("/sample")
#        else:
#            return render(request, 'form.html', {'form': data})
#    else:
#        print("get")
#    form_person = PersonForm()
#    return render(request, 'form.html', {'form': form_person})
