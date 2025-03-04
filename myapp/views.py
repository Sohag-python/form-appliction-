from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

# View to list all contacts
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'myapp/contact_list.html', {'contacts': contacts})

# View to add a new contact
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'myapp/contact_form.html', {'form': form})

# View to delete a contact
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'myapp/contact_confirm_delete.html', {'contact': contact})