import os
import time
from appium import webdriver


class Inicializar_App():
    basedirApp = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    Json = basedirApp + u'\json'

    #Environment = 'TEST'

    Navegador = u'ANDROID'

    Path_Evidencias = basedirApp + u'/data/capturas'

    '''if Environment == 'TEST':
        DRIVER = {
            "platformName": "Android",
            "platformVersion": "8",
            "deviceName": "on5xelte",
            "automationName": "UiAutomator1",
            "appPackage": "com.clarodrive.android",
            "appActivity": "com.owncloud.android.ui.authentication.AuthenticatorActivity"
        }

        DRIVER = webdriver.Remote('http://127.0.0.1:4723/wd/hub', DRIVER)
        time.sleep(10)'''



    #if Environment == 'PROD':
