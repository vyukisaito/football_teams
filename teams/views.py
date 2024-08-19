from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from teams.models import Team
from teams.forms import TeamsForm


@method_decorator(login_required(login_url='login'), name='dispatch')
class TeamListView(ListView):
    model = Team
    template_name = 'teams.html'
    context_object_name = 'teams'

    def get_queryset(self):
        teams = super().get_queryset().order_by('team')
        search = self.request.GET.get('search')
        if search:
            teams = teams.filter(team__icontains=search)
        return teams


@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateTeamView(CreateView):
    model = Team
    form_class = TeamsForm
    template_name = 'new_team.html'
    success_url = '/teams/'


class DetailTeamView(DetailView):
    model = Team
    template_name = 'teams_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateTeamView(UpdateView):
    model = Team
    form_class = TeamsForm
    template_name = 'teams_update.html'

    def get_success_url(self):
        return reverse_lazy('teams_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteTeamView(DeleteView):
    model = Team
    template_name = 'teams_delete.html'
    success_url = '/teams/'
