import pytest

from .models import Group, Person


@pytest.mark.django_db
def test_add_admin_to_members():
    """
    make sure that a group's admin is added to members
    """
    john = Person.objects.create(name="John")
    group = Group.objects.create(admin=john)
    assert john in group.members.all()
