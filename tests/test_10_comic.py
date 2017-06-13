#!/usr/bin/env python
# encoding: utf-8

import logging
from unittest import TestCase

import cleanup
import stampy.plugin.alias
import stampy.plugin.karma
import stampy.stampy

logger = logging.getLogger(__name__)


class TestStampy(TestCase):
    cleanup.clean()

    def test_comiclist(self):
        messages = [{u'message': {u'date': 1478361249, u'text': u'/comic list',
                              u'from': {u'username': u'iranzo',
                                        u'first_name': u'Pablo',
                                        u'last_name': u'Iranzo G\xf3mez',
                                        u'id': 5812695}, u'message_id': 108,
                              u'chat': {u'all_members_are_administrators': True,
                                        u'type': u'group', u'id': -158164217,
                                        u'title': u'BOTdevel'}},
                 u'update_id': 837253571}]
        stampy.stampy.process(messages)

    def test_comicall(self):
        messages = [{u'message': {u'date': 1478361249, u'text': u'/comic',
                              u'from': {u'username': u'iranzo',
                                        u'first_name': u'Pablo',
                                        u'last_name': u'Iranzo G\xf3mez',
                                        u'id': 5812695}, u'message_id': 108,
                              u'chat': {u'all_members_are_administrators': True,
                                        u'type': u'group', u'id': -158164217,
                                        u'title': u'BOTdevel'}},
                 u'update_id': 837253571}]
        stampy.stampy.process(messages)

    def test_comictrigger(self):
        messages = [{u'message': {u'date': 1478361249, u'text': u'/comic trigger',
                              u'from': {u'username': u'iranzo',
                                        u'first_name': u'Pablo',
                                        u'last_name': u'Iranzo G\xf3mez',
                                        u'id': 5812695}, u'message_id': 108,
                              u'chat': {u'all_members_are_administrators': True,
                                        u'type': u'group', u'id': -158164217,
                                        u'title': u'BOTdevel'}},
                 u'update_id': 837253571}]
        stampy.stampy.process(messages)

