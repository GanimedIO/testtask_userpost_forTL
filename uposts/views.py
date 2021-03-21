import json
import requests
from django.http import HttpResponse
from django.db import models
from uposts.models import Posts
from uposts.models import Company
from uposts.models import Geo
from uposts.models import Address
from uposts.models import Users
from django.views import generic



class IndexView(generic.ListView):
    template_name = 'C:/ddd/userpost/uposts/templates/uposts/index.html'
    context_object_name = 'posts_list'
    def get_queryset(self):
        #return Posts.objects.all()
        return Posts.objects.all()

