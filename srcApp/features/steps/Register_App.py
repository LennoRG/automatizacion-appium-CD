# -*- coding: utf-8 -*-
from behave import *
from selenium.webdriver.common.by import By

from fuctions.Functions_App import Functions_App as Register
import time

use_step_matcher("re")


class Register_App(Register):
    @given("Open the aplication CD")
    def abrir_App(self):
        Register.abrir_Aplicacion(self)


    @when("I charge the Json of the app: register_App\.json")
    def cargo_JSON(self):
        Register.get_json_file(self, "register_App")

    @then("I click on the button REGISTRATE new user")
    def step_impl(self):
        self.driver.find_element_by_xpath("//android.view.View[@content-desc='REGÍSTRATE']").click()
        time.sleep(3)

    @then("I click on the button Email")
    def step_impl(self):
        Register.get_elements(self, "opcion _register_Email").click()
        time.sleep(2)

    @step("I enter the user data, email and password")
    def step_impl(self):
        correoUser = "testautomatizadoapp04@getnada.com"
        contraseña = "Qa654321$"

        Register.get_elements(self, "input_CorreoElectronico").send_keys(correoUser)
        Register.get_elements(self, "input_passw").send_keys(contraseña)
        time.sleep(1)


    @then("I click on mostrar/ocultar password")
    def step_impl(self):
        Register.get_elements(self, "opcion_Mostrar/Ocultar").click()
        time.sleep(2)

        Register.get_elements(self, "opcion_Mostrar/Ocultar").click()
        time.sleep(2)


    @then("I click on the button REGISTRARME")
    def step_impl(self):
        Register.get_elements(self, "btn_REGISTRARME").click()
        time.sleep(3)


    @step("I choose the TDC payment method")
    def step_impl(self):
        Register.get_elements(self, "opcion_plan_TDC").click()
        time.sleep(3)


    @then("I choose the 200GB plan")
    def step_impl(self):
        Register.get_elements(self, "opcion_plan_200GB").click()
        time.sleep(2)


    @step("I click on the button ACEPTAR")
    def step_impl(self):
        Register.get_elements(self, "btn_ACEPTAR_plan").click()
        time.sleep(2)


    @then("I enter the credit card information")
    def step_impl(self):
        nombreTitular = "Claro drive"
        numTDC = "4523984527360876"
        mesTDC = "01"
        anioTDC = "22"
        cvvTDC = "698"

        Register.get_elements(self, "input_NombreTitutar_TDC").send_keys(nombreTitular)
        time.sleep(1)
        Register.get_elements(self, "input_NumTarjeta_TDC").send_keys(numTDC)
        Register.get_elements(self, "input_MMM_TDC").send_keys(mesTDC)
        time.sleep(1)
        Register.get_elements(self, "input_AA_TDC").send_keys(anioTDC)
        time.sleep(1)
        Register.get_elements(self, "input_CVV_TDC").send_keys(cvvTDC)
        time.sleep(3)


    @step("I click on the button ACEPTAR the tdc")
    def step_impl(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View/android.view.View[6]/android.widget.Image[1]").click()
        time.sleep(2)

        Register.get_elements(self, "btn_ACEPTAR_TDC").click()
        time.sleep(30)


    @then("I click on the button IR A MI CLARO DRIVE")
    def step_impl(self):
        Register.get_elements(self, "btn_IR_A_MI_CLARO_DRIVE").click()
        time.sleep(3)


    @when("The Wizard is displayed, I validate the text and I click the COMENZAR button")
    def step_impl(self):
        Register.get_elements(self, "popup_btn_RECHAZAR").click()
        time.sleep(7)

        self.Texto_WizardMAS = self.driver.find_elements(By.XPATH,
                                                         "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
        self.count = 0

        for self.WizardMAS in self.Texto_WizardMAS:
            RESULTADO_TEXTO = ['Descubre las funciones principales de Claro drive con éste tutorial.']
            assert RESULTADO_TEXTO[self.count] == self.WizardMAS.text, "EL TEXTO NO COINCIDE"
            print(RESULTADO_TEXTO)

        Register.get_elements(self, "wizard_btn_COMENZAR").click()
        time.sleep(3)


    @then("The Wizard is displayed on the Crear option, I validate the text I click on the SIGUIENTE button")
    def step_impl(self):
        self.Texto_WizardCREAR = self.driver.find_elements(By.XPATH,
                                                           "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
        self.count = 0

        for self.WizardCREAR in self.Texto_WizardCREAR:
            RESULTADO_TEXTO = ['Sube a Claro drive todos tus archivos, fotos y videos. Escanea y sube tus archivos.']
            assert RESULTADO_TEXTO[self.count] == self.WizardCREAR.text, "EL TEXTO NO COINCIDE"
            print(RESULTADO_TEXTO)

        Register.get_elements(self,  "wizard_btn_SIGUIENTE").click()
        time.sleep(3)


    @then("The Wizard is displayed on the Favoritos option, I validate the text I click on the SIGUIENTE button")
    def step_impl(self):
        self.Texto_WizardFAVORITOS = self.driver.find_elements(By.XPATH,
                                                           "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
        self.count = 0

        for self.WizardFAVORITOS in self.Texto_WizardFAVORITOS:
            RESULTADO_TEXTO = ['Encuentra aquí tus archivos o carpetas que hayas marcado como favoritos.']
            assert RESULTADO_TEXTO[self.count] == self.WizardFAVORITOS.text, "EL TEXTO NO COINCIDE"

        Register.get_elements(self, "wizard_btn_SIGUIENTE").click()
        time.sleep(3)


    @then("The Wizard is displayed on the Galeria option, I validate the text I click on the FINALIZAR button")
    def step_impl(self):
        self.Texto_WizardGALERIA = self.driver.find_elements(By.XPATH,
                                                             "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
        self.count = 0

        for self.WizardGALERIA in self.Texto_WizardGALERIA:
            RESULTADO_TEXTO = ['Encuentra tus imágenes y videos que hayas sincronizado previamente en la galería de Claro drive.']
            assert RESULTADO_TEXTO[self.count] == self.WizardGALERIA.text, "EL TEXTO NO COINCIDE"

        Register.get_elements(self, "wizard_btn_FINALIZAR").click()
        time.sleep(3)

