from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse

def index(request):
    latest_question_list=Question.objects.all()
    context={'latest_question_list':latest_question_list}
    return render(request, 'polls_app/index.html',context)

def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    context={'question':question}
    return render(request,'polls_app/detail.html',context)

def result(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    context={'question':question}
    return render(request,'polls_app/result.html',context)

def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls_app/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls_app:result', args=(question.id,)))