from django.db import transaction
from rest_framework import serializers
from rest_framework.filters import BaseFilterBackend

from .models import Event, Reference, Contestant, Project, Winner


class EventNestedFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(event_id=view.kwargs['event_pk'])


class ReferenceSerializer(serializers.ModelSerializer):
    """Reference Serializer"""

    class Meta:
        model = Reference
        fields = ['id', 'url']


class ContestantSerializer(serializers.ModelSerializer):
    """Contestant Serializer"""

    class Meta:
        model = Contestant
        fields = ['id', 'name']


class ProjectSerializer(serializers.ModelSerializer):
    """Project Serializer"""

    class Meta:
        model = Project
        fields = ['id', 'name']


class WinnerSerializer(serializers.ModelSerializer):
    """Winner Serializer"""

    class Meta:
        model = Winner
        fields = ['id', 'name']


class EventSerializer(serializers.ModelSerializer):
    """Event Serializer"""
    references = ReferenceSerializer(many=True, required=False)
    winners = WinnerSerializer(many=True, required=False)
    contestants = ContestantSerializer(many=True, required=False)
    projects = ProjectSerializer(many=True, required=False)

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'about',
            'contact',
            'date',
            'references',
            'winners',
            'contestants',
            'projects'
        ]

    @transaction.atomic
    def create(self, validated_data):
        references = validated_data.pop('references', [])
        projects = validated_data.pop('projects', [])
        winners = validated_data.pop('winners', [])
        contestants = validated_data.pop('contestants', [])
        event = Event.objects.create(**validated_data)
        ref_items = []
        pro_items = []
        win_items = []
        con_items = []
        for reference in references:
            ref_item = Reference(url=reference['url'], event=event)
            ref_items.append(ref_item)
        for project in projects:
            pro_item = Project(name=project['name'], event=event)
            pro_items.append(pro_item)
        for winner in winners:
            win_item = Winner(name=winner['name'], event=event)
            win_items.append(win_item)
        for contestant in contestants:
            con_item = Contestant(name=contestant['name'], event=event)
            con_items.append(con_item)
        Contestant.objects.bulk_create(con_items)
        Winner.objects.bulk_create(win_items)
        Project.objects.bulk_create(pro_items)
        Reference.objects.bulk_create(ref_items)
        return event
