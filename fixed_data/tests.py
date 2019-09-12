import unittest
from django.urls import reverse
from django.test import Client
from .models import Client, Technology, Service, Building, Link
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


def create_client(**kwargs):
    defaults = {}
    defaults["phone_no"] = "phone_no"
    defaults["updated_at"] = "updated_at"
    defaults["is_active"] = "is_active"
    defaults.update(**kwargs)
    if "created_by" not in defaults:
        defaults["created_by"] = create_'users_customuser'()
    return Client.objects.create(**defaults)


def create_technology(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return Technology.objects.create(**defaults)


def create_service(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "technology" not in defaults:
        defaults["technology"] = create_technology()
    return Service.objects.create(**defaults)


def create_building(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return Building.objects.create(**defaults)


def create_link(**kwargs):
    defaults = {}
    defaults["circuit_id"] = "circuit_id"
    defaults.update(**kwargs)
    if "service" not in defaults:
        defaults["service"] = create_service()
    if "client" not in defaults:
        defaults["client"] = create_client ()
    if "building" not in defaults:
        defaults["building"] = create_ building ()
    return Link.objects.create(**defaults)


class ClientViewTest(unittest.TestCase):
    '''
    Tests for Client
    '''
    def setUp(self):
        self.client = Client()

    def test_list_client(self):
        url = reverse('app_name_client_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_client(self):
        url = reverse('app_name_client_create')
        data = {
            "phone_no": "phone_no",
            "updated_at": "updated_at",
            "is_active": "is_active",
            "created_by": create_'users_customuser'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_client(self):
        client = create_client()
        url = reverse('app_name_client_detail', args=[client.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_client(self):
        client = create_client()
        data = {
            "phone_no": "phone_no",
            "updated_at": "updated_at",
            "is_active": "is_active",
            "created_by": create_'users_customuser'().pk,
        }
        url = reverse('app_name_client_update', args=[client.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class TechnologyViewTest(unittest.TestCase):
    '''
    Tests for Technology
    '''
    def setUp(self):
        self.client = Client()

    def test_list_technology(self):
        url = reverse('app_name_technology_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_technology(self):
        url = reverse('app_name_technology_create')
        data = {
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_technology(self):
        technology = create_technology()
        url = reverse('app_name_technology_detail', args=[technology.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_technology(self):
        technology = create_technology()
        data = {
        }
        url = reverse('app_name_technology_update', args=[technology.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ServiceViewTest(unittest.TestCase):
    '''
    Tests for Service
    '''
    def setUp(self):
        self.client = Client()

    def test_list_service(self):
        url = reverse('app_name_service_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_service(self):
        url = reverse('app_name_service_create')
        data = {
            "technology": create_technology().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_service(self):
        service = create_service()
        url = reverse('app_name_service_detail', args=[service.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_service(self):
        service = create_service()
        data = {
            "technology": create_technology().pk,
        }
        url = reverse('app_name_service_update', args=[service.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class BuildingViewTest(unittest.TestCase):
    '''
    Tests for Building
    '''
    def setUp(self):
        self.client = Client()

    def test_list_building(self):
        url = reverse('app_name_building_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_building(self):
        url = reverse('app_name_building_create')
        data = {
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_building(self):
        building = create_building()
        url = reverse('app_name_building_detail', args=[building.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_building(self):
        building = create_building()
        data = {
        }
        url = reverse('app_name_building_update', args=[building.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class LinkViewTest(unittest.TestCase):
    '''
    Tests for Link
    '''
    def setUp(self):
        self.client = Client()

    def test_list_link(self):
        url = reverse('app_name_link_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_link(self):
        url = reverse('app_name_link_create')
        data = {
            "circuit_id": "circuit_id",
            "service": create_service().pk,
            "client": create_client ().pk,
            "building": create_ building ().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_link(self):
        link = create_link()
        url = reverse('app_name_link_detail', args=[link.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_link(self):
        link = create_link()
        data = {
            "circuit_id": "circuit_id",
            "service": create_service().pk,
            "client": create_client ().pk,
            "building": create_ building ().pk,
        }
        url = reverse('app_name_link_update', args=[link.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


