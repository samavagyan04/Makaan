from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *

class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request) :
        maininfo = MainInfo.objects.first()
        homestatus=HomeStatus.objects.all()
        imagecycle=ImageCycle.objects.first()
        propertytypes=PropertyTypes.objects.all()
        propertytypesjarang=PropertyTypesJarang.objects.all()
        moreinformation= MoreInformation.objects.all()
        propertylisting=PropertyListing.objects.all()
        contactagent=ContactAgent.objects.all()
        propertyagent=PropertyAgent.objects.all()
        client=Client.objects.all()
        gallery=Gallery.objects.all()

        context = {
            'maininfo':maininfo,
            'homestatus':homestatus,
            'imagecycle':imagecycle,
            'propertytypes':propertytypes,
            'propertytypesjarang':propertytypesjarang,
            'moreinformation':moreinformation,
            'propertylisting':propertylisting,
            'contactagent':contactagent,
            'propertyagent':propertyagent,
            'client':client,
            'gallery':gallery
                  }

        return render(request,self.template_name,context)
    
class AboutListView(ListView):
    template_name='about.html'


    def get(self, request) :
        aboutstatus=AboutStatus.objects.all()


        context={
            'aboutstatus':aboutstatus
        }

        return render(request,self.template_name,context)