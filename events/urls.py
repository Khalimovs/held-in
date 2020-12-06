from itertools import chain

from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from .views import (
    EventViewSet,
    ContestantViewSet,
    ProjectViewSet,
    ReferenceViewSet,
    WinnerViewSet
)

simple_router = SimpleRouter()
simple_router.register('events', EventViewSet, basename='events')

router = SimpleRouter()
temp_parent_router = SimpleRouter()
temp_parent_router.register(r'events', EventViewSet, basename="events")

event_router = routers.NestedSimpleRouter(temp_parent_router, r'events', lookup='event')
event_router.register(r'winners', WinnerViewSet, basename='winners')
event_router.register(r'references', ReferenceViewSet, basename='references')
event_router.register(r'contestants', ContestantViewSet, basename='contestants')
event_router.register(r'projects', ProjectViewSet, basename='projects')

urlpatterns = list(
    chain(
        simple_router.urls,
        router.urls,
        temp_parent_router.urls,
        event_router.urls,
    )
)
