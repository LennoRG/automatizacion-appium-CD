import time

from appium import webdriver

driver = {
  "platformName": "Android",
  "platformVersion": "8",
  "deviceName": "on5xelte",
  "automationName": "UiAutomator1",
  "appPackage": "com.clarodrive.android",
  "appActivity": "com.owncloud.android.ui.authentication.AuthenticatorActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', driver)
time.sleep(10)
driver.find_element_by_xpath("//android.view.View[@content-desc='100 GB SIN COSTO CON TELCEL O TELMEX']").click()
time.sleep(5)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View").click()
time.sleep(5)
driver.find_element_by_xpath("//android.view.View[@content-desc='REGÍSTRATE']").click()
time.sleep(5)
