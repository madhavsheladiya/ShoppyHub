from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contacting = form.save()
        return render(request, 'contact/contacted.html', {'contact': contacting})
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})