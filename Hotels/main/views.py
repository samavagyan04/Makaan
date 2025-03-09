from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.core.mail import EmailMessage
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from Hotels.settings import EMAIL_HOST_USER
from django.contrib.auth.mixins import LoginRequiredMixin


def RegisterPage(request):
    template_name = 'register.html'

    form = UserCreationForm
    message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.email = request.POST.get("email")
            obj.save()
            emailll = EmailMessage(
                subject = f'Hello {request.POST.get("username")}',
                body = 'Sign up completed succesfully',
                from_email=EMAIL_HOST_USER,
                to = [request.POST.get('email')]
            )
            emailll.send()
            return redirect('login')
        else:
            message = form.errors
    
    context = {
        'message':message,
        'form':form,
    }

    return render(request,template_name,context)
    

def LoginPage(request):
    template_name = 'login.html'

    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            message = 'user not found'
    
    context = {'message':message}

    return render(request,template_name,context)


def Logout(request):
    logout(request)
    return redirect('login')
    


def MainInfoF(context,title,subtitle):
    context['maininfo'] = MainInfo.objects.get()
    context['aboutstatus'] = AboutStatus.objects.all()
    context['gallery'] = Gallery.objects.all()
    context['subtitle'] = subtitle
    context['title'] = title


def SearchItem(request):
    word = request.GET.get('q')
    loc_q = request.GET.get('l')
    goall = request.GET.get('goall')
    proplisting = PropertyListing.objects.filter(name__icontains = word,adress__icontains = loc_q,npatak = goall)
    statusinfo = HomeStatus.objects.all()
    imgcycle = ImageCycle.objects.get()
    propertyTypesJarang = PropertyTypesJarang.objects.all()
    moreinformation = MoreInformation.objects.all()
    contactagent = ContactAgent.objects.all()
    propertyagent = PropertyAgent.objects.all()
    client = Client.objects.all()
    context = {
        'statusinfo':statusinfo,
        'imgcycle':imgcycle,
        'propertyTypesJarang':propertyTypesJarang,
        'moreinformation':moreinformation,
        'proplisting':proplisting,
        'contactagent':contactagent,
        'propertyagent':propertyagent,
        'client':client,
                }
    MainInfoF(context,'home','')
    

    return render(request,'index.html',context)



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
        

        context={
            'aboutstatus':aboutstatus,
            'maininfo': maininfo,
            'moreinformation':moreinformation,
            'contactagent':contactagent,
            'propertyagent':propertyagent,
            
           

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
    
    def post(self,request):
        form = AddPropertyForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pr_list')
        else:
            print(form.errors)
            form = AddPropertyForm()
        propertylisting = PropertyListing.objects.all()
        contactagent = ContactAgent.objects.all()

        context = {
            'propertylisting':propertylisting,
            'contactagent':contactagent,
            'form':form,
                  }

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

#----------------------------------------------------------------------

class PropertyAgents(ListView):
    template_name='property-agent.html'

    def get(self,request):
        propertyagent=PropertyAgent.objects.all()
        contactagent=ContactAgent.objects.all()

        context={
            'propertyagent':propertyagent,
            'contactagent':contactagent
        }
        MainInfoF(context,'Property Agent','Property Agent')

        return render(request,self.template_name,context)
    
#-------------------------------------------------------------------------
    
class Testimonial(ListView):
    template_name='testimonial.html'

    def get(self,request):
        client=Client.objects.all()

        context={
            'client':client
        }
        MainInfoF(context,'Testimonial','Testimonial')

        return render(request,self.template_name,context)

#-------------------------------------------------------------------------

class ContactPage(DetailView):
    template_name = 'contact.html'


    def get(self, request):
        if request.user.is_authenticated:
            name = request.user.username
            email = request.user.email
        else:
            name = ''
            email = ''

        form = ContactForm()

        context = {
            'form':form,
            'name':name,
            'email':email
                  }
        MainInfoF(context,'contact','Contact Us')
        return render(request,self.template_name,context)
    
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = ContactForm()


        context = {
            'form':form,


                  }

        MainInfoF(context,'contact','Contact Us')
        return render(request,self.template_name,context)

