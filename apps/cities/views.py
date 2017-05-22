from django.views.generic import FormView


class TemplateFormView(FormView):
    template_name = 'form.html'
