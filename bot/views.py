from django.shortcuts import render, redirect
from .models import Grades, Subjects, Question
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm
from .serializer import Questiondata
from rest_framework import viewsets
# Create your views here.


class Questionapi(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('question')
    serializer_class = Questiondata

def home(request):
    answers = Question.objects.all()
    context = {'answers': answers}

    return render(request, 'home.html', context=context)


def ans(request, pk):
    answer = Question.objects.get(bot_id=pk)
    context = {'answer': answer}

    return render(request, 'answer.html', context=context)


def askquestion(request):
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/')

    context = {'form': form}
    return render(request, 'askquestion.html', context=context)


def edit_answer(request, pk):
    answer = Question.objects.get(bot_id=pk)
    form = QuestionForm(instance=answer)

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=answer)
        if form.is_valid():
            print(form.data)
            form.save()

            return redirect('ans', pk=pk)

    context = {'answer': answer, 'form': form}
    return render(request, 'askquestion.html', context=context)
