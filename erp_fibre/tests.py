from django.test import TestCase

# Create your tests here.
import unittest
from django.urls import reverse
from django.test import Client
from .models import FTTHProject
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_ftthproject(**kwargs):
    defaults = {}
    defaults["project_name"] = "project_name"
    defaults["description"] = "description"
    defaults["initial_kmz"] = "initial_kmz"
    defaults["is_acknowledged"] = "is_acknowledged"
    defaults["updated_at"] = "updated_at"
    defaults["is_active"] = "is_active"
    defaults.update(**kwargs)
    return FTTHProject.objects.create(**defaults)


class FTTHProjectViewTest(unittest.TestCase):
    '''
    Tests for FTTHProject
    '''
    def setUp(self):
        self.client = Client()

    def test_list_ftthproject(self):
        url = reverse('erpProject_ftthproject_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_ftthproject(self):
        url = reverse('erpProject_ftthproject_create')
        data = {
            "project_name": "project_name",
            "description": "description",
            "initial_kmz": "initial_kmz",
            "is_acknowledged": "is_acknowledged",
            "updated_at": "updated_at",
            "is_active": "is_active",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_ftthproject(self):
        ftthproject = create_ftthproject()
        url = reverse('erpProject_ftthproject_detail', args=[ftthproject.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_ftthproject(self):
        ftthproject = create_ftthproject()
        data = {
            "project_name": "project_name",
            "description": "description",
            "initial_kmz": "initial_kmz",
            "is_acknowledged": "is_acknowledged",
            "updated_at": "updated_at",
            "is_active": "is_active",
        }
        url = reverse('erpProject_ftthproject_update', args=[ftthproject.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
