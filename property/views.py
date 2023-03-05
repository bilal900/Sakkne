from django.shortcuts import redirect, render
from django.views.generic.edit import FormMixin
from .form import PropertyBookForm 
from .filters import PropertyFilters  
from django_filters.views import FilterView




# Create your views here.
from django.views.generic import ListView,DetailView
from .models import Property

class PropertyList(FilterView):
 model=Property
 paginate_by=1
 filterset_class=PropertyFilters
 template_name='property/property_list.html'
class PropertyDetail(FormMixin,DetailView):
  model=Property
  form_class=PropertyBookForm

  def get_context_data(self, **kwargs):  ##related category#get_context_data
    context =super().get_context_data(**kwargs)
    context["related"] =Property.objects.filter(category=self.get_object().category)[:2]
    return context
  
  def post(self,request,*args,**kwargs):
    form=self.get_form()
    if form.is_valid():
      myform=form.save(commit=False)
      myform.property=self.get_object()
      myform.user=request.user
      myform.save()

      return redirect('/')


