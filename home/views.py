from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages

from django.views.decorators.cache import never_cache

from django.contrib.auth.decorators import login_required


