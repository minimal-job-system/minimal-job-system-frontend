from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone

from django.contrib.auth.mixins import LoginRequiredMixin

from django_filters.views import FilterView

from datetime import timedelta

from job_system_api.models import JobTemplate, Job, JobParameter, JobLogEntry
from job_system_frontend.forms import JobForm, JobParameterFormSet
from job_system_frontend import settings


def index(request):
    return HttpResponse(
        "<h1>Welcome to the Minimal Job System Web Application</h1>"
    )


class JobListView(FilterView):
    model = Job
    queryset = Job.objects.filter(
        date_created__gte=timezone.now()-timedelta(days=30)
    )
    ordering = ["-date_created"]
    filter_fields = ('owner',)

    template_name = "job_system_frontend/job_list.html"

    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        context['is_system_user'] = \
            self.request.user.groups.filter(name='jobsys').exists()
        context['only_owner_can_stop_job'] = settings.ONLY_OWNER_CAN_STOP_JOB
        context['log_levels'] = \
            JobLogEntry._meta.get_field('level').flatchoices
        return context


class JobRegisterView(LoginRequiredMixin, TemplateView):
    template_name = 'job_system_frontend/job_register.html'
    success_url = reverse_lazy('job_system_frontend:job_list')

    def get_context_data(self, **kwargs):
        context = super(JobRegisterView, self).get_context_data(**kwargs)
        context['parameter_types'] = \
            JobParameter._meta.get_field('type').flatchoices
        context['job_templates'] = JobTemplate.objects.all()

        if self.request.POST:
            context['selected_job_template'] = \
                self.request.POST["job_templates"]
            context['job_form'] = JobForm(self.request.POST)
            context['job_parameter_form_set'] = \
                JobParameterFormSet(self.request.POST)
        else:
            context['selected_job_template'] = -1
            context['job_form'] = JobForm()
            context['job_parameter_form_set'] = JobParameterFormSet()

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """

        context = self.get_context_data()
        job_form = context['job_form']
        job_parameter_form_set = context['job_parameter_form_set']

        if not all([job_form.is_valid(), job_parameter_form_set.is_valid()]):
            context.update({
                'job_form': job_form
            })
            context.update({
                'job_parameter_form_set': job_parameter_form_set
            })
            return self.render_to_response(context)

        with transaction.atomic():
            self.job = job_form.save()
            job_parameter_form_set.instance = self.job
            job_parameter_form_set.save()
            return HttpResponseRedirect(str(self.success_url))


"""
class JobDetailView(DetailView):
    model = Job


class JobUpdateView(UpdateView):
    model = Job
    success_url = reverse_lazy('job_system_frontend:job_list')
    fields = ['name']

    def get_context_data(self, **kwargs):
        context = super(JobUpdateView, self).get_context_data(**kwargs)
        return context

class JobDeleteView(DeleteView):
    model = Job
    success_url = reverse_lazy('job_system_frontend:job_list')

    def get_context_data(self, **kwargs):
        context = super(JobDeleteView, self).get_context_data(**kwargs)
        return context
"""
