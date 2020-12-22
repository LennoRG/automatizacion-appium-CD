# -*- coding: utf-8 -*-
import time

from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from fuctions.Functions_App import Functions_App as Landing

from srcApp.fuctions import Inicializar_App
from selenium.webdriver.android import webdriver
from selenium import webdriver
use_step_matcher("re")

class Landing_App(Landing):

    @given("Open the aplication")
    def step_impl(self):
        Landing.abrir_Aplicacion(self)


    @when("I charge the Json of the app: landingApp\.json")
    def cargo_json(self):
        Landing.get_json_file(self, "landingApp")



    @then("I click on the button Registrate Gratis")
    def btn_RegisterGratris(self):

        self.TEXTO_PRINCIPAL = self.driver.find_elements(By.XPATH,
                                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View[1]")
        self.count = 0
        for self.txtPrin in self.TEXTO_PRINCIPAL:
            RESULTADO_TEXTO = ['Tus archivos donde quieras, cuando quieras.']
            assert RESULTADO_TEXTO[self.count] == self.txtPrin.text, "LOS TEXTOS NO COINCIDEN"
            print(RESULTADO_TEXTO)

            time.sleep(3)

        Landing.get_elements(self, "RegistrarGratis").click()
        time.sleep(3)


    @step("I click on the icon return to landing")
    def logo_CD(self):
        Landing.get_elements(self, "Logo_CD_Landing").click()
        time.sleep(5)


    @then("I click on the button REGISTRATE")
    def btn_Register(self):
        self.driver.find_element_by_xpath("//android.view.View[@content-desc='REGÍSTRATE']").click()
        time.sleep(3)

    @then("I click on the button INICIA SESION")
    def btn_Login(self):
        self.driver.find_element(By.XPATH,
                                 "//android.view.View[@content-desc='INICIA SESIÓN']").click()
        time.sleep(3)

    @then("I click on the link Ayuda")
    def step_impl(self):
        Landing.get_elements(self, "link_Ayuda").click()
        time.sleep(3)

    @step("I click on the button Categorias")
    def step_impl(self):
        #assert Landing.get_text(self, "txt_Ayuda") == "Centro de ayuda"
        #time.sleep(1)
        self.TEXTO_AYUDA = self.driver.find_elements(By.XPATH,
                                                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]")
        self.count = 0
        for self.txtAyuda in self.TEXTO_AYUDA:
            RESULTADO_TEXTO = ['Centro de ayuda']
            assert RESULTADO_TEXTO[self.count] == self.txtAyuda.text, "LOS texto no coincide"
            print(RESULTADO_TEXTO)

            time.sleep(3)
            
        Landing.get_elements(self, "ayuda_Categorias").click()
        time.sleep(3)


    @then("I click on the button Volver")
    def step_impl(self):
        Landing.get_elements(self, "btn_ayuda_Volver").click()
        time.sleep(3)



    @then("I click on the Paises combox and compare names")
    def step_impl(self):
        Landing.get_elements(self, "combox_Paises").click()
        time.sleep(3)

        Landing.get_elements(self, "combox_Paises").click()
        time.sleep(3)

        '''#COMPARO LOS NOMBRES DENTRO DEL COMBOX PAISES
        self.NOMBRE_PAISES = self.driver.find_elements(By.XPATH,
                                                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[2]")
        self.count = 0

        for self.NomPais in self.NOMBRE_PAISES:
            RESULTADO_NOM_PAISES = ['México', 'Colombia', 'Brasil', 'Guatemala',
                                    'Honduras', 'Nicaragua', 'El Salvador', 'Costa Rica',
                                    'Perú', 'Argentina', 'Panamá', 'Chile',
                                    'Ecuador', 'Puerto Rico', 'República Dominicana', 'Uruguay',
                                    'Paraguay']
            assert RESULTADO_NOM_PAISES[self.count] == self.NomPais.text, "LOS NOMBRE DE LOS PAISES NO COINCIDEN"
            print(RESULTADO_NOM_PAISES)
            self.count = self.count + 1
            time.sleep(3)'''


    @then("I click on the link CLARO DRIVE NEGOCIO")
    def step_impl(self):
        Landing.get_elements(self, "link_Negocio").click()
        time.sleep(3)


    @then("I click on the link CLARO DRIVE PERSONAL")
    def step_impl(self):
        Landing.get_elements(self, "link_CDPersonal").click()
        time.sleep(3)