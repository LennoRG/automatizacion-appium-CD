# Created by Lenno at 18/12/2020
Feature: Registro de usuario en la App CD
  # Enter feature description here

  Scenario: Flujo Registro de Usuario
    Given Open the aplication CD
    When I charge the Json of the app: register_App.json
    Then I click on the button REGISTRATE new user
    Then I click on the button Email
    And I enter the user data, email and password
    Then I click on mostrar/ocultar password
    Then I click on the button REGISTRARME
    And I choose the TDC payment method
    Then I choose the 200GB plan
    And I click on the button ACEPTAR
    Then I enter the credit card information
    And I click on the button ACEPTAR the tdc
    Then I click on the button IR A MI CLARO DRIVE

    #OPCIONES FLUJO WIZARD
    When The Wizard is displayed, I validate the text and I click the COMENZAR button
    Then The Wizard is displayed on the Crear option, I validate the text I click on the SIGUIENTE button
    Then The Wizard is displayed on the Favoritos option, I validate the text I click on the SIGUIENTE button
    Then The Wizard is displayed on the Galeria option, I validate the text I click on the FINALIZAR button
