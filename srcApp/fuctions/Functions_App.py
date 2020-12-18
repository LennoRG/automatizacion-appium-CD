# -*- coding: utf-8 -*-
import json
import os
import time

import pytest
import self as self
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.android import webdriver
from selenium.webdriver.support.select import Select
from selenium import webdriver

from behave.model import Scenario

from fuctions.Inicializar_App import Inicializar_App


class Functions_App(Inicializar_App):

    def abrir_Aplicacion(self,navegador=Inicializar_App.Navegador):

        Environment = 'TEST'
        if Environment == 'TEST':
            driver = {
                "platformName": "Android",
                "platformVersion": "8",
                "deviceName": "on5xelte",
                "automationName": "UiAutomator1",
                "appPackage": "com.clarodrive.android",
                "appActivity": "com.owncloud.android.ui.authentication.AuthenticatorActivity"
            }

            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)
            time.sleep(10)

        print(Inicializar_App.basedirApp)
        self.ventanas = {}
        print("-------------------")
        print(navegador)
        print("-------------------")

        if navegador == ("Android"):

            self.ventanas ={'Principal': self.driver.window_handles[0]}
            return self.driver

    def teardDown(self):
        print("SE CERRRO CON EXITO EL DRIVER")
        self.driver.quit()


    def get_json_file(self, file):
        json_path = Inicializar_App.Json + "/" + file + '.json'
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print("get_json_file: " + json_path)
        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"get_json_file: No se encontro el archivo " + file)
            Functions_App.teardDown(self)

    def get_entity(self, entity):
        if self.json_strings is False:
            print("Esta Entity no Existe")
        else:
            try:
                self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
                self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
                return True
            except KeyError:
                pytest.skip(u"get_entity: No se encontro la key a la cual hace referencia: " + entity)
                Functions_App.teardDown(self)
                return None

    def get_elements(self, entity, MyTextElement=None):
        Get_Entity = Functions_App.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor del Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_element_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_partial_link_text(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                print("get_elements: " + self.json_ValueToFind)
                return elements

            except NoSuchElementException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                Functions_App.teardDown(self)
            except TimeoutError:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                Functions_App.teardDown(self)

    def get_text(self, entity, MyTextElement = None):
        Get_Entity = Functions_App.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor del Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element_by_id(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element_by_name(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)
                    elements = self.driver.find_elements_by_xpath(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element_by_partial_link_text(self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element_by_css_selector(self.json_ValueToFind)

                print("get_text: " + self.json_ValueToFind)
                print("Text Value : " + elements.text)
                return elements.text
            except NoSuchElementException:
                print("get_text:  No se encontro el elemento: " + self.json_ValueToFind)
                Functions_App.teardDown(self)
            except TimeoutException:
                print("get_text: No se encontro el elemento: " + self.json_ValueToFind)
                Functions_App.teardDown(self)

    def get_select_elements(self, entity):
        Get_Entity = Functions_App.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")

        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    select = Select(self.driver.find_element_by_id(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "name":
                    select = Select(self.driver.find_element_by_name(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "xpath":
                    select = Select(self.driver.find_element_by_partial_link_text(self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "link":
                    select = Select(self.driver.find_element_by_partial_link_text(self.json_ValueToFind))

                print("get_select_elements: " + self.json_ValueToFind)
                return select

            except NoSuchElementException:
                print("No se encontro ele elemento: " + self.json_ValueToFind)
                Functions_App.teardDown(self)
            except TimeoutException:
                print("No se encontro el elemento: " + self.json_ValueToFind)
                Functions_App.teardDown(self)








