# Created by Lenno at 22/12/2020
Feature: Automatizacion del Buzon CD App
  # Enter feature description here

  Scenario: Flujo Buzon App
    Given Open the aplication to enter
    When I charge the Json of the app: buzon_App
    Then I click on the button INICIA SESIÓN
    And I click on the button login Email
    Then enter the user data to login
    Then I click on the button INICIA SESION login
