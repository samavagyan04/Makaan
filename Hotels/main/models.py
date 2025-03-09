from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class MainInfo(models.Model):
    img = models.ImageField('Image',upload_to='main_image')
    name = models.CharField('Company name',max_length=255)
    address = models.CharField('Address',max_length=255)
    phone = PhoneNumberField('Phonenumber')
    email = models.EmailField('Email')
    twitter = models.URLField('Twitter')
    facebook = models.URLField('facebook')
    youtube = models.URLField('youtube')
    linkedin = models.URLField('linkedin')


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Main Info'
        verbose_name_plural = 'Main Info'

class HomeStatus(models.Model):
    text1=models.CharField('text1',max_length=255)
    text2=models.CharField('text2',max_length=255,null=True)
    text3=models.CharField('text3',max_length=255,null=True)
    text4=models.CharField('text4',max_length=255,null=True)
    buton_text=models.CharField('buton_text',max_length=255)

class ImageCycle(models.Model):
    img1=models.ImageField('img1',upload_to='img1',null = True)
    img2=models.ImageField('img2',upload_to='img2',null = True)


class PropertyTypes(models.Model):
    title=models.CharField('title',max_length=255)
    text=models.TextField('text')
    
    def __str__(self) -> str:
        return self.title
    
class PropertyTypesJarang(models.Model):
    img=models.ImageField('Img',upload_to='icon_image')
    names=models.CharField('names',max_length=255)
    properties=models.CharField('properties',max_length=250)

    def __str__(self) -> str:
        return self.names
    
class MoreInformation(models.Model):
    imgs=models.ImageField('Imgs',upload_to='home_image')
    vernagir=models.CharField('vernagir',max_length=255)
    texts=models.TextField('texts')

    def __str__(self) -> str:
        return self.vernagir


class PropertyListing(models.Model):
    img=models.ImageField('img',upload_to='img')
    name=models.CharField('name',max_length=255)
    npatak=models.CharField('npatak',max_length=255)
    price=models.FloatField('price')
    information=models.CharField('information',max_length=255)
    adress=models.CharField('adress',max_length=255)
    taracq=models.FloatField('taracq')
    bed=models.IntegerField('bed')
    bath=models.IntegerField('bath')

    def __str__(self):
        return self.name
    
class ContactAgent(models.Model):
    imgagent=models.ImageField('imgagent',upload_to='imgagent')
    ver=models.CharField('ver',max_length=255)
    text=models.CharField('text',max_length=255)


class PropertyAgent(models.Model):
    agentimg=models.ImageField('agentimg',upload_to='agentimg')
    facebook=models.URLField('facebook')
    twitter=models.URLField('twitter')
    instagram=models.URLField('instagram')
    name=models.CharField('name',max_length=255)
    designation=models.CharField('designation',max_length=255)


class Client(models.Model):
    comment=models.TextField('comment')
    imgclient=models.ImageField('imgclient',upload_to='imgclient')
    name=models.CharField('name',max_length=255)
    profession=models.CharField('profession',max_length=255)

class Gallery(models.Model):
    images = models.ImageField('Gallery',upload_to='images')

    def __str__(self):
        return 'Gallery'

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------


class AboutStatus(models.Model):
    img = models.ImageField('image',upload_to='images')
    text = models.CharField('Some text',max_length=255)
    word1 = models.CharField('word1',max_length=255)
    word2 = models.CharField('word2',max_length=255)
    word3 = models.CharField('word3',max_length=255)

    def __str__(self):
        return 'AboutStatus'
    
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

class ContactModel(models.Model):
    name = models.CharField('Your name',max_length=255,blank=True)
    email = models.EmailField('Your Email',blank=True)
    subject = models.CharField('Subject',max_length=255)
    message = models.TextField('Message')

    def __str__(self):
        return self.name