from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.base import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Problems, Notate
from .forms import ProblemCreateForm, AddNotateForm, ProblemEditForm, EditNotateForm
from .filters import ProductFilter
# Create your views here.

class MyProblemView(View):

    def get(self, request):
        problems = Problems.objects.filter(user=request.user)
        # Фільтри
        filter = ProductFilter(request.GET, queryset=problems)
        problems = filter.qs
        # Пагінація
        paginator = Paginator(problems, 10)
        page = request.GET.get('page', 1)
        try:
            problems = paginator.page(page)
        except PageNotAnInteger:
            problems = paginator.page(1)
        except EmptyPage:
            problems = paginator.page(paginator.num_pages)

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


class DetailProblemView(View):

    def get(self, request, slug):
        form = AddNotateForm(request.POST)
        problem = Problems.objects.get(slug=slug)
        if problem.user.pk == request.user.pk:
            context = {
                'problem': problem,
                'form' : form
            }

            return render(request, 'problems/problem_detail.html', context)
        return redirect('problems')

    def post(self, request, slug):
        problem = Problems.objects.get(slug=slug)
        form = AddNotateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.problem = problem
            form.save()
            return redirect("problems")
        return render(request, 'problems/problem_detail.html', {'form': form})


class EditProblemView(View):

    def get(self, request, slug):
        problem = Problems.objects.get(slug=slug)
        form = ProblemEditForm(instance=problem)
        context = {
            'editform': form
        }
        return render(request, 'problems/edit_problem.html', context)

    def post(self, request, slug):
        problem = Problems.objects.get(slug=slug)
        form = ProblemEditForm(instance=problem, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('problems')
        context = {
            'editform': form
        }
        return render(request, 'problems/edit_problem.html', context)


class DeleteProblemView(View):

    def get(self, request, slug):
        problem = Problems.objects.get(slug=slug)
        problem.delete()
        return redirect('problems')


class EditNotateView(View):

    def get(self, request, notate_id):
        notate = Notate.objects.get(pk=notate_id)
        form = EditNotateForm(instance=notate)
        context = {
            'editform': form
        }
        return render(request, 'problems/edit_notate.html', context)

    def post(self, request, notate_id):
        notate = Notate.objects.get(pk=notate_id)
        form = EditNotateForm(instance=notate, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('problems')
        context = {
            'editform': form
        }
        return render(request, 'problems/edit_notate.html', context)


class DeleteNotateView(View):

    def get(self, request, notate_id):
        notate = Notate.objects.get(pk=notate_id)
        notate.delete()
        return redirect('problems')
