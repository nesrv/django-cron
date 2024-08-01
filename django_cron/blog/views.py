from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForm
# from .tasks import write_file
from .service import send

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'    
    template_name = 'blog/contact.html'
    

    def form_valid(self, form):
        form.save()
        send(form.instance.email)

        # write_file.delay(form.instance.email)
        return super().form_valid(form)

