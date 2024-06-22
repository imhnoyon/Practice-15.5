from django.shortcuts import render,redirect
from . import forms,models

# Create your views here.
def album(request):
    if request.method=='POST':
        data=forms.AlbumModelForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('album')
        
    else:
        data=forms.AlbumModelForm()
    return render(request,'album.html',{'form':data})


def home(request):
    data=models.AlbumForm.objects.all()
    return render(request,'home.html',{'form':data})




def edited(request,id):
    edit=models.AlbumForm.objects.get(pk=id)
    edits_form=forms.AlbumModelForm(instance=edit)
    if request.method=='POST':
        edits_form=forms.AlbumModelForm(request.POST,instance=edit)
        if edits_form.is_valid():
            edits_form.save()
            return redirect('homepages')
        
    return render(request,'album.html',{'form':edits_form})


def deleted(request,id):
    del_func=models.AlbumForm.objects.get(pk=id)
    del_func.delete()
    return redirect('homepages')


