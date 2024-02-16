from django.shortcuts import render
import random 
from django.conf import settings
import os
from django.views.generic import View
from django.http import HttpResponse

class LogView(View):
    def get(self, request):
        return render(request, 'index.html')


class GenerateRandomDataView(View):
    def get(self, request):
        log_file_path = os.path.join(settings.BASE_DIR, 'test.log')
        L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
        random_line = (random.choice(L))
        with open(log_file_path, "a") as file: 
            file.writelines(random_line)
        return HttpResponse(f'{random_line} added to log')
