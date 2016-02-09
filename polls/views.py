from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import Question

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request,'polls/index.html',context)


def detail(request, question_id):
    return HttpResponse("esta es la pregunta numero %s." % question_id)

def results(request, question_id):
    response = "Este es el resultado de la pregunta %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Estas votando en la pregunta %s." % question_id)
