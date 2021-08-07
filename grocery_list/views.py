from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, UpdateView, DeleteView, CreateView

from grocery_list.forms import GroceryListForm
from grocery_list.models import GroceryList


class GroceryListView(ListView):
    template_name = 'grocery_list/index.html'
    context_object_name = "grocery_list"

    def get_queryset(self):
        print(self.request.user)
        return GroceryList.objects.filter(user=self.request.user)

    def post(self, request):
        form_date = request.POST.get("date")
        grocery_list = GroceryList.objects.filter(user=self.request.user, date=form_date)
        return render(request, self.template_name, {"grocery_list": grocery_list})


class GroceryView(FormView):
    form_class = GroceryListForm
    template_name = 'grocery_list/update.html'

    def get(self, request, **kwargs):
        instance = GroceryList.objects.get(pk=kwargs['pk'])
        form = self.form_class(instance=instance)
        return render(request, self.template_name, {"form": form})

    def form_valid(self, form):
        form.save()
        return redirect('grocery:index')

    def post(self, request, *args, **kwargs):
        instance = GroceryList.objects.get(pk=kwargs['pk'])
        form = self.form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save(self.request.user)
            form.save()
            return redirect('grocery:index')
        return render(request, self.template_name, {"form": form})


class GroceryDeleteView(DeleteView):
    model = GroceryList
    success_url = reverse_lazy('grocery:index')


class GroceryCreateView(CreateView):
    model = GroceryList
    template_name = 'grocery_list/update.html'
    form_class = GroceryListForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(self.request.user)
            form.save()
            return redirect('grocery:index')
        return render(request, self.template_name, {"form": form})
