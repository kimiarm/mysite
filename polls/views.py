from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from .models import Question
from django.urls import reverse
from django.template import loader , RequestContext
from django.template.loader import render_to_string
# Create your views here.
def index(request) :
    latest_questions =  Question.objects.order_by('-pub_date')[:5]


    # context = RequestContext(request ,  {
    #
    #     'latest_questions' : latest_questions
    # })
    # context_dict = context.flatten()
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context_dict))

    contex = {'latest_questions' : latest_questions}
    return render(request , 'polls/index.html' , contex)

def detail(request , question_id):
        # question =  Question.objects.get(pk = question_id)
        question = get_object_or_404( Question , pk = question_id)
        return render(request , 'polls/detail.html' , {'question' : question})
def results(request , question_id):
    print("fffwff")
    question = get_object_or_404(Question , pk=question_id)
    return render(request , 'polls/results.html' , {'question' :question})

def votes(request , question_id):
    question = get_object_or_404(Question , pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request , 'polls/detail.html' , {'question' : question , 'error_message' : "Please select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results' , args=(question_id,)))


