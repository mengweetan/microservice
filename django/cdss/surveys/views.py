from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, FormView, DetailView, View
from django.http import JsonResponse, HttpResponseRedirect, request, HttpResponse, FileResponse
from .models import *
# Create your views here.
class Prep_data(TemplateView):
    #model = SMS_record
    template_name = "survey_form.html"
#context_object_name = "sms"
    def dispatch(self, request, *args, **kwargs):

        self.ward = self.kwargs['pk']
        self.block = request.GET.get('block')
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print (self.ward )
        print (self.block )
        try:
            q = survey.objects.filter(loc=self.ward ).filter(block=self.block )
            print ('query')
            print (q[0])
            print (q[0].data)
            context['data'] = '{}'.format(q[0].data.get('data'))


        except:
            context['data']= 'nothing'
        return context
