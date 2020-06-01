from django.urls import path
from sim_project.sim_app.views import Tasks, ActivePower, ReactivePower

urlpatterns = [
  path('tasks/init-sim', Tasks.as_view()),
  path('reads/active-power', ActivePower.as_view()),
  path('reads/reactive-power', ReactivePower.as_view()),
]