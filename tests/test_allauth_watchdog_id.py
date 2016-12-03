#!/usr/bin/env python
# -*- coding: utf-8 -*-

from allauth.socialaccount.tests import OAuth2TestsMixin
from allauth.tests import MockedResponse, TestCase
from allauth_watchdog_id.provider import WatchdogProvider
from django.test import Client, TestCase


class WatchdogTests(OAuth2TestsMixin, TestCase):
    provider_id = WatchdogProvider.id

    def get_mocked_response(self):
        return MockedResponse(200, """
            {"username":"a",
            "name":"",
            "absolute_url":"http://id.siecobywatelska.pl/users/a/",
            "visible_name":"a",
            "avatars":{"80":"https://secure.gravatar.com/avatar/daff4e13fdf8cea5729221d2ba17b7c8.jpg?s=80&r=g&d=mm",
            "50":"https://secure.gravatar.com/avatar/daff4e13fdf8cea5729221d2ba17b7c8.jpg?s=50&r=g&d=mm",
            "150":"https://secure.gravatar.com/avatar/daff4e13fdf8cea5729221d2ba17b7c8.jpg?s=150&r=g&d=mm"},
            "email":"a@jawnosc.tk"}""")
