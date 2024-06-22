from django.shortcuts import render,redirect
from . import forms,models
# Create your views here.

def musician(request):
    if request.method=='POST':
        data=forms.MusicianModelForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('musician')
        
    else:
         data=forms.MusicianModelForm()
    return render(request,'musician.html',{'form':data})


def edited(request,id):
    edit=models.MusicianForm.objects.get(pk=id)
    edits_form=forms.MusicianModelForm(instance=edit)
    if request.method=='POST':
        edits_form=forms.MusicianModelForm(request.POST,instance=edit)
        if edits_form.is_valid():
            edits_form.save()
            return redirect('homepages')
        
    return render(request,'musician.html',{'form':edits_form})
            








