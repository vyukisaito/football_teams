from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from teams.views import TeamListView, CreateTeamView, DetailTeamView, UpdateTeamView, DeleteTeamView
from accounts.views import register_view, login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout_team'),
    path('register/', register_view, name='register'),
    path('teams/', TeamListView.as_view(), name='teams_list'),
    path('new_teams/', CreateTeamView.as_view(), name='new_team'),
    path('teams/<int:pk>/', DetailTeamView.as_view(), name='teams_detail'),
    path('teams/<int:pk>/update', UpdateTeamView.as_view(), name='teams_update'),
    path('teams/<int:pk>/delete', DeleteTeamView.as_view(), name='teams_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
