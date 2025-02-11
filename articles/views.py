from django.shortcuts import render
from .models import Girls,Locations
from django.views.generic import DetailView,ListView
from app.utils import common_data
class GirlsDetailViews(DetailView):
    model = Girls
    template_name = 'post.html'
    context_object_name = 'girls'
    def get_context_data(self, **kwargs):
        context=super(GirlsDetailViews, self).get_context_data(**kwargs)
        context.update(common_data())
        context['title']=self.object.name
        return context