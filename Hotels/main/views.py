from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *




def MainInfoF(context,title,subtitle):
    context['maininfo'] = MainInfo.objects.get()
    context['aboutstatus'] = AboutStatus.objects.all()
    context['gallery'] = Gallery.objects.all()
    context['subtitle'] = subtitle
    context['title'] = title



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
    
#----------------------------------------------------------------------

class AboutListView(ListView):
    template_name='about.html'


    def get(self, request) :
        aboutstatus=AboutStatus.objects.all()
        maininfo = MainInfo.objects.first()
        moreinformation= MoreInformation.objects.all()
        contactagent=ContactAgent.objects.all()
        propertyagent=PropertyAgent.objects.all()
        gallery=Gallery.objects.all()

        context={
            'aboutstatus':aboutstatus,
            'maininfo': maininfo,
            'moreinformation':moreinformation,
            'contactagent':contactagent,
            'propertyagent':propertyagent,
            'gallery':gallery
           

        }
        MainInfoF(context,'about','About Us')

        return render(request,self.template_name,context)
    

#-------------------------------------------------------------

class PropertyListView(ListView):
    template_name='property-list.html'

    def get(self,request):
        propertylisting=PropertyListing.objects.all()
        contactagent=ContactAgent.objects.all()


        context={
            'propertylisting':propertylisting,
            'contactagent':contactagent
            }
        MainInfoF(context,'Property List','Property List')

        return render(request,self.template_name,context)
    
#----------------------------------------------------------------

class PropertyType(ListView):
    template_name='property-type.html'

    def get(self,request):
        propertytypes=PropertyTypes.objects.all()
        propertytypesjarang=PropertyTypesJarang.objects.all()


        context={
            'propertytypes':propertytypes,
            'propertytypesjarang':propertytypesjarang,
        }
        MainInfoF(context,'Property Type','Property Type')
        return render(request,self.template_name,context)
