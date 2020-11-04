from django.shortcuts import render
from testapp.models import Company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class CompanyListView(ListView):
    model=Company
    #default template_name:company_list.html
    #default context_object_name:company_list


class CompanyDetailView(DetailView):
    model=Company
    

    #default template_name:company_detail.html
    #default context_object_name:company or object

class CompanyCreateView(CreateView):
    model=Company
    fields=('name','location','ceo')
        #default template_name:company_form.html

class CompanyUpdateView(UpdateView):
    model=Company
    fields=('name','ceo')

class CompanyDeleteView(DeleteView):
    model=Company
    success_url=reverse_lazy('companies')
