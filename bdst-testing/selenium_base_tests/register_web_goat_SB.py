# -*- coding: utf-8 -*-
from seleniumbase import BaseCase


class RegisterWebGoat(BaseCase):

    def test_register_web_goat(self):
        self.open('http://localhost:8080/WebGoat/registration')
        self.update_text('#username', 'testuser')
        self.update_text('#password', 'testpw')
        self.update_text('#matchingPassword', 'testpw')
        self.click('[name="agree"]')
        self.click("//button[@type='submit']")
