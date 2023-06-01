from django.shortcuts import render, redirect
from django.contrib.auth import login
from typing import Any, Dict, Optional
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator

from .forms import SignUpForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email')
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')


    def get_object(self, queryset: QuerySet[Any] | None = ...):
        return self.request.user
