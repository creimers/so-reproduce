from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Person(models.Model):
    name = models.CharField(max_length=20)


class Group(models.Model):
    admin = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="group_admin"
    )
    members = models.ManyToManyField(Person, related_name="group_members", blank=True)


@receiver(post_save, sender=Group)
def add_admin_to_members(sender, instance, created, **kwargs):
    """
    adds self.admin to self.members when Group is created
    """

    if created and instance.admin:
        instance.members.add(instance.admin)
