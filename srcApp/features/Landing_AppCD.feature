# Created by Lenno at 28/09/2020
Feature: Landing de la aplicacion movil Claro drive
  # Enter feature description here

  Scenario: Landing de la App Claro drive
    Given Open the aplication
    When I charge the Json of the app: landingApp.json
    Then I click on the button Registrate Gratis
    And I click on the icon return to landing
    Then I click on the button REGISTRATE
    And I click on the icon return to landing
    Then I click on the button INICIA SESION
    And I click on the icon return to landing

    Then I click on the link Ayuda
    And I click on the button Categorias
    Then I click on the button Volver

    Then I click on the Paises combox and compare names

    Then I click on the link CLARO DRIVE NEGOCIO
    Then I click on the link CLARO DRIVE PERSONAL