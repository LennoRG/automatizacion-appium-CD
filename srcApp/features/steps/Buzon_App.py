# -*- coding: utf-8 -*-

from behave import *
from selenium.webdriver.common.by import By

from fuctions.Functions_App import Functions_App as Buzon
import time

use_step_matcher("re")

class Buzon_App(Buzon):
    @given("Open the aplication to enter")
    def consumo_Json(self):
        Buzon.abrir_Aplicacion(self)


    @when("I charge the Json of the app: buzon_App")
    def step_impl(self):
        Buzon.get_json_file(self, "buzon_App")


    @then("I click on the button INICIA SESIÓN")
    def step_impl(self):
        self.driver.find_element(By.XPATH,
                                 "//android.view.View[@content-desc='INICIA SESIÓN']").click()
        time.sleep(3)


    @step("I click on the button login Email")
    def step_impl(self):
        Buzon.get_elements(self, "btn_Email_Login").click()
        time.sleep(3)



    @then("enter the user data to login")
    def step_impl(self):
        correo_User = "testautomatizadoapp04@getnada.com"
        passw_User = "Qa654321$"

        Buzon.get_elements(self, "ipunt_Correo_User").send_keys(correo_User)
        Buzon.get_elements(self, "ipunt_Passw_User").send_keys(passw_User)
        time.sleep(3)

        Buzon.get_elements(self, "opcion_Mostrar/Ocultar").click()
        time.sleep(2)


    @then("I click on the button INICIA SESION login")
    def step_impl(self):
        Buzon.get_elements(self, "btn_Inicio_Sesion").click()
        time.sleep(5)