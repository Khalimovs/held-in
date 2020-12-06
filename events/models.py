from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField(max_length=3000, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:50]

    class Meta:
        ordering = ('-date',)


class Winner(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(
        Event,
        related_name='winner_events',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name[:40]


class Contestant(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(
        Event,
        related_name='participated_events',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name[:40]


class Reference(models.Model):
    url = models.URLField(max_length=500)
    event = models.ForeignKey(
        Event,
        related_name='+',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.url[:40]


class Project(models.Model):
    name = models.CharField(max_length=500)
    event = models.ForeignKey(
        Event,
        related_name='+',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name[:40]
