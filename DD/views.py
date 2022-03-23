import datetime
import json
import os
import subprocess
import time

# from PIL import Image
# import PIL

from django.core.files.storage import FileSystemStorage
# from docx import opendocx, getdocumenttext
# import docx2txt
# import mammoth
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from D import settings
from DD.forms import ProfilePic
from DD.models import User, Subjects, Groups, Theory, Task, Practice

import projectq
from subprocess import Popen, PIPE


def index(request):
    context = get_current_user_info(request)
    return render(request, 'Profile.html', context=context)


def get_current_user_info(request):
    try:
        user = User.objects.get(email=request.user.email)
        context = {
            'user': user,
            'name': 'images/' + request.user.username + '.png'
        }
        return context
    except:
        context = {
            'error': "User doesn't exist",
        }
        return render(request, 'login.html', context=context)


class MyFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name):
        if os.path.exists(self.path(name)):
            os.remove(self.path(name))
        return name


@csrf_exempt
def profile_pic(request):
    if request.method == 'POST':
        files = request.FILES['files']
        fss = FileSystemStorage(location='DD/static/images')
        name = request.user.username + '.png'
        if fss.exists(name):
            fss.delete(name)
        file = fss.save(name, files)
        User.objects.filter(email=request.user.email).update(photo=name)
        file_url = fss.url(file)
    user = User.objects.get(email=request.user.email)
    context = {
        'user': user,
        'name': 'images/' + request.user.username + '.png'
    }
    return render(request, 'Profile.html', context=context)


def subjects(request):
    subject = Subjects.objects.all()
    theories = Theory.objects.all()
    groups = Groups.objects.all()
    tasks = Task.objects.all()
    context = {
        'subject': subject,
        'theories': theories,
        'groups': groups,
        'tasks': tasks,
    }
    return render(request, 'Subjects.html', context=context)


@csrf_exempt
def update_subject(request):
    try:
        Subjects.objects.filter(title=request.POST['subject-title']).update(description=request.POST['subject-description'])
        subject = Subjects.objects.all()
        theories = Theory.objects.all()
        groups = Groups.objects.all()
        tasks = Task.objects.all()
        context = {
            'subject': subject,
            'theories': theories,
            'groups': groups,
            'tasks': tasks,
        }
        return render(request, 'Subjects.html', context=context)
    except:
        return HttpResponse('Something wrong')


@csrf_exempt
def get_specific_subject(request):
    subject = Subjects.objects.all()
    data = json.loads(request.POST.get('data'))
    subject1 = Subjects.objects.get(title=data['value'])
    theories = Theory.objects.filter(subject=subject1.title)
    tasks = Task.objects.all()
    context = {
        'subject': subject,
        'subject1': subject1,
        'theories': theories,
        'tasks': tasks,
    }
    return render(request, 'Subjects.html', context=context)


@csrf_exempt
def load_selected_theory(request):
    selected_theory = Theory.objects.get(title=request.POST['theory-title'])
    subject = Subjects.objects.all()
    context = {
        'theory': selected_theory,
        'file_path': "theory/" + selected_theory.title + ".docx",
        'subject': subject,
    }
    return render(request, 'Theory.html', context=context)


@csrf_exempt
def add_new_theory(request):
    subject = Subjects.objects.all()
    context = {
        'subject': subject,
    }
    return render(request, 'Theory.html', context=context)


@csrf_exempt
def new_theory(request):
    title = request.POST['new-title']
    subject = request.POST['new-subject']
    summary = request.POST['new-summary']
    group = Groups.objects.get(title=request.POST['new-group'])
    files = request.FILES['files']
    fss = FileSystemStorage(location='DD/static/theory')
    name = title + '.docx'
    if fss.exists(name):
        fss.delete(name)
    fss.save(name, files)
    t = Theory.objects.create(title=title, \
                          doc=name, \
                          upload_date='2021-12-05', \
                          subject=subject, \
                          assigned_groups=group, \
                          summary=summary)
    t.save()
    selected_theory = Theory.objects.get(title=title)
    context = {
        'theory': selected_theory,
        'file_path': "theory/" + selected_theory.title + ".docx",
    }
    return render(request, 'Theory.html', context=context)


@csrf_exempt
def load_selected_task(request):
    selected_task = Task.objects.get(name=request.POST['task-title'])
    subject = Subjects.objects.all()
    context = {
        'task': selected_task,
        'subject': subject,
    }
    return render(request, 'Task.html', context=context)


def groups(request):
    return render(request, 'Groups.html')


def practice(request):
    practice = Practice.objects.all()
    context = {
        'practice': practice,
    }
    return render(request, 'Practice.html', context=context)


@csrf_exempt
def run_practice(request):
    # name = 'Shor'
    from .static.practice import Shor
    #process = subprocess.call(['python', 'DD/static/practice/Shor.py'], stdout=PIPE, stderr=PIPE)
    # stdout, stderr = process.communicate()

    # data = subprocess.call("python DD/static/practice/Shor.py", shell=True)
    # time.sleep(32)
    selected_practice = Practice.objects.get(title="Shor's Algorithm")
    practice = Practice.objects.all()
    number = request.POST['number']
    data = Shor.run(number)
    context = {
        'data': data,
        'pr': selected_practice,
        'practice': practice,
    }
    return render(request, 'Practice.html', context=context)


def profile(request):
    context = get_current_user_info(request)
    return render(request, 'Profile.html', context=context)


def theory(request):
    return render(request, 'Theory.html')


def login(request):
    return render(request, 'Login.html')


"""@csrf_exempt
def check_login_data(request):
    try:
        data = json.loads(request.POST.get('login_data'))
        user_email = User.objects.get(email=data['email'])
        user_password = User.objects.get(password=data['password'])
        if user_email == data['']
        for users_with_bonuses in data:
            username_who_received = data[users_with_bonuses][0]
            anonymous = data[users_with_bonuses][4]
            username_who_sent = request.user.username
            real_name_who_received = data[users_with_bonuses][1]
            bonus = data[users_with_bonuses][2]
            comment = data[users_with_bonuses][3]
            real_name_who_sent = data[users_with_bonuses][5]
            date = datetime.date.today()
            # Add BonusesWithComments
            new_user_with_bonus = BonusesWithComments(username_who_received=username_who_received,
                                                      username_who_sent=username_who_sent, bonus=bonus,
                                                      comment=comment, date=date, anonymous=anonymous,
                                                      real_name_who_received=real_name_who_received,
                                                      real_name_who_sent=real_name_who_sent)
            new_user_with_bonus.save()
            # general_bonuses = ReceivedBonuses.objects.get(username=username_who_received)
            # colleague_quantity_of_bonus_id = general_bonuses.id
            # colleague_quantity_of_bonus = general_bonuses.bonus_colleague
            # admin_quantity_of_bonus = general_bonuses.bonus_admin
            '''ReceivedBonuses(id=colleague_quantity_of_bonus_id, username=username_who_received, 
                            bonus_admin=admin_quantity_of_bonus, 
                            bonus_colleague=int(colleague_quantity_of_bonus)+int(bonus)).save()'''
        # Update ReceivedBonuses
        general_bonuses = ReceivedBonuses.objects.get(username=request.user.username)
        general_bonuses.bonus_admin = 0
        general_bonuses.save()
        return HttpResponse('Success')
    except TypeError:
        return HttpResponse('Json...again...Here?')"""
