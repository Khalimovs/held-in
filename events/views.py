from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .models import (
    Event,
    Reference,
    Contestant,
    Winner,
    Project
)
from .serializers import (
    EventSerializer,
    ReferenceSerializer,
    ProjectSerializer,
    ContestantSerializer,
    WinnerSerializer,
    EventNestedFilterBackend
)


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        return super(self.__class__, self).get_permissions()


class ReferenceViewSet(ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    filter_backends = [EventNestedFilterBackend]

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        return super(self.__class__, self).get_permissions()


class ContestantViewSet(ModelViewSet):
    queryset = Contestant.objects.all()
    serializer_class = ContestantSerializer
    filter_backends = [EventNestedFilterBackend]

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        return super(self.__class__, self).get_permissions()


class WinnerViewSet(ModelViewSet):
    queryset = Winner.objects.all()
    serializer_class = WinnerSerializer
    filter_backends = [EventNestedFilterBackend]

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        return super(self.__class__, self).get_permissions()


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [EventNestedFilterBackend]

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = []
        else:
            self.permission_classes = [IsAuthenticated, IsAdminUser]
        return super(self.__class__, self).get_permissions()
