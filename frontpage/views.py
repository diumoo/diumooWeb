from django.shortcuts import render_to_response
from diumooWeb.sparkle.models import Application,Version
from diumooWeb.frontpage.models import *

def index(request):
    app=Application.objects.all()
    if len(app)>0:
        app=app[0]
        versions=app.versions.order_by('-published')
        if len(versions)>0:
            current_version=versions.filter(active=True)
            if len(current_version)>0:
                current_version=current_version[0]
                update_date=current_version.published
    features=Feature.objects.order_by('-rank').all()
    notices=Notice.objects.order_by('-rank').all()
    links=Link.objects.all()
    screenshots=ScreenShot.objects.all()
    return render_to_response('index.html',locals())

def sponsors(request):
    app=Application.objects.all()
    if len(app)>0:
        app=app[0]
        versions=app.versions.order_by('-published')
        if len(versions)>0:
            current_version=versions.filter(active=True)
            if len(current_version)>0:
                current_version=current_version[0]
                update_date=current_version.published
    links=Link.objects.all()
    sponsor_cates=SponsorCate.objects.order_by('rank').all()
    return render_to_response('sponsor_list.html',locals())

def donate(request):
    app=Application.objects.all()
    if len(app)>0:
        app=app[0]
        versions=app.versions.order_by('-published')
        if len(versions)>0:
            current_version=versions.filter(active=True)
            if len(current_version)>0: 
                current_version=current_version[0]
                update_date=current_version.published
    links=Link.objects.all()
    return render_to_response('donate.html',locals())

def qa(request):
    app=Application.objects.all()
    if len(app)>0:
        app=app[0]
        versions=app.versions.order_by('-published')
        if len(versions)>0:
            current_version=versions.filter(active=True)
            if len(current_version)>0: 
                current_version=current_version[0]
                update_date=current_version.published
    links=Link.objects.all()
    qas=QA.objects.all()
    return render_to_response('qa.html',locals())
