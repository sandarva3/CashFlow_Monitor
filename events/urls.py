from django.urls import path
from .views import(
    events_view,
    addevent_view,
    eventitems_view,
    eitemsadd_view,
    eitemremove_view,
    editevent_view,
)


urlpatterns = [
    path('', events_view, name='events'),
    path('addevent/', addevent_view, name='addevent'),
    path('eventitems/<int:id>/', eventitems_view, name='eventitems'),
    path('eitemadd/<int:id>/', eitemsadd_view, name='eitemadd'),
    path('eitemremove/<int:id>/<int:eid>', eitemremove_view, name='eitemremove'),
    path('editevent/<int:id>/', editevent_view, name='editevent'),
]