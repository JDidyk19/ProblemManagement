from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.base import View
from .models import Problems
from .forms import ProblemCreateForm
from .filters import ProductFilter
# Create your views here.

class MyProblemView(View):

    def get(self, request):
        problems = Problems.objects.filter(user=request.user)
        filter = ProductFilter(request.GET, queryset=problems)
        problems = filter.qs
        context = {
            'problems': problems,
            'filter': filter,
        }
        return render(request, 'problems/problems.html', context)


class AddProblemView(View):

    def get(self, request):
        form = ProblemCreateForm(request.POST or None, request.FILES or None)
        context = {
            'addform' : form
        }
        return render(request, 'problems/add_problem.html', context)

    def post(self, request):
        form = ProblemCreateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.save()
            return redirect('problems')
        context = {
            'addform': form
        }
        return render(request, 'problems/add_problem.html', context)

class DeleteProblemView(View):

    def get(self, request, slug):
        problem = Problems.objects.get(slug=slug)
        problem.delete()
        return redirect('problems')
