# -*- coding: utf-8 -*-
from seleniumbase import BaseCase


class UntitledTestCase(BaseCase):

    def test_untitled_test_case(self):
        self.open('http://hackazon.webscantest.com/')
        self.click("link=Sign In / Sign Up")
        self.click("link=New user?")
        self.click('[name="searchString"]')
        self.click('#first_name')
        self.update_text('#first_name', 'user')
        self.click('#last_name')
        self.update_text('#last_name', 'user2')
        self.click('#username')
        self.update_text('#username', 'bla')
        self.click('#email')
        self.update_text('#email', 'bla@foo.bar')
        self.click('#password')
        self.update_text('#password', 'ggg')
        self.click('#password_confirmation')
        self.update_text('#password_confirmation', 'ggg')
        self.click("//input[@value='Register']")
