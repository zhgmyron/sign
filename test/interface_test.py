# -*- coding: UTF-8 -*-
import requests
import unittest
import json
class GetEventlistTest(unittest.TestCase):
    def setUp(self):
        self.url="http://127.0.0.1:8000/api/get_event_list/"
    def test_get_evvent_null(self):
        r= requests.get(self.url,params={'eid':''})
        result = r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],"parameter error")
    def test_get_event_error(self):
        r =requests.get(self.url,params={'eid':'20'})
        result= r.json()
        self.assertEqual(result['status'],10022)
        self.assertEqual(result['message'],"query result is empty")

    def test_get_event_success(self):
        r =requests.get(self.url,params={'eid':'1'})
        result= r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],"success")
