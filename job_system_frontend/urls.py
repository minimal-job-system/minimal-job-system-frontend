from django.conf.urls import url, include
from django.http import HttpResponseRedirect

from job_system_frontend.views import index, JobListView, JobRegisterView
    #, JobDetailView, JobUpdateView, JobDeleteView


app_name = "job_system_frontend"
urlpatterns = [
    url(r'^$', lambda r: HttpResponseRedirect('jobs/')),
    url(r'^index$', index, name="index"),
    # url(r'^admin/sync_job_tmpl$', sync_job_tmpl, name="sync_job_tmpl"),
    url(r'jobs/$', JobListView.as_view(), name="job_list"),
    url(r'jobs/register$', JobRegisterView.as_view(), name="job_register"),
    # url(r'jobs/(?P<pk>[0-9]+)/$', JobDetailView.as_view(), name='jobs_detail'),
    # url(r'jobs/(?P<pk>[0-9]+)/update$', JobUpdateView.as_view(), name='jobs_update'),
    # url(r'jobs/(?P<pk>[0-9]+)/delete$', JobDeleteView.as_view(), name='jobs_delete'),
]
