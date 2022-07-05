from django.views.generic import TemplateView


class IndexView(TemplateView):
    """View responsável pela página inicial"""

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Enterprise Management System"
        return context


# class CreateEntityView(TemplateView):

#     # Template name
