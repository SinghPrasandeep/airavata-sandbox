from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from .models import Request
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'dashboard/index.html'
    context_object_name = 'all_requests'

    def get_queryset(self):
        return Request.objects.all()

class ReviewerView(generic.ListView):
    template_name = 'dashboard/reviewer.html'
    context_object_name = 'all_requests'

    def get_queryset(self):
        return Request.objects.all()


class AdminView(generic.ListView):
    template_name = 'dashboard/admin.html'
    context_object_name = 'all_requests'

    def get_queryset(self):
        return Request.objects.all()

class AdminRequestView(generic.ListView):
    model = Request
    template_name = 'dashboard/admin-request-view.html'




class DetailView(generic.DetailView):
    model = Request
    template_name = 'dashboard/detail.html'


class RequestCreate(CreateView):
    model = Request
    fields = ['request_title', 'request_status', 'request_description', 'allocation_type',
              'applications_to_be_used', 'disk_usage_range_per_job', 'document', 'field_of_science',
              'keywords', 'max_memory_per_cpu', 'num_cpus_per_job', 'request_reviewed_and_funded_by',
              'request_date', 'service_units', 'specific_resource_selection', 'typical_su_per_job']


class RequestUpdate(UpdateView):
    model = Request
    fields = ['request_title', 'request_status', 'request_description', 'allocation_type',
              'applications_to_be_used', 'disk_usage_range_per_job', 'document', 'field_of_science',
              'keywords', 'max_memory_per_cpu', 'num_cpus_per_job', 'request_reviewed_and_funded_by',
              'request_date', 'service_units', 'specific_resource_selection', 'typical_su_per_job']

class RequestDelete(DeleteView):
    model = Request
    success_url = reverse_lazy('dashboard:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'dashboard/registration_form.html'


    # Display a blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard:index')
        return render(request, self.template_name, {'form': form})

