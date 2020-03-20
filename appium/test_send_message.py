# -*- coding: utf-8 -*-
import pytest
from appium import webdriver


@pytest.mark.parametrize("udid, systemPort", [
       ("localhost:4321", "8201"),
       ("localhost:4322", "8202"),
       ("localhost:4323", "8203"),
       ]
)
def test_send_message(udid, systemPort, getAPKPath):

   capabilities = {
       'platformName': 'Android',
       'deviceName': 'Genymotion Cloud SaaS Devices',
       'app': getAPKPath,
       'udid': udid,
       'systemPort': systemPort,
       'automationName': 'UiAutomator2',
       'noReset': True,
   }
   url = 'http://localhost:4723/wd/hub'
   driver = webdriver.Remote(url, capabilities)

   txt_ipt = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tcarpentier.myAndroidApp:id/editText")')
   txt_ipt.clear()
   txt_ipt.send_keys("It's a trap!")

   send_btn = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tcarpentier.myAndroidApp:id/button")')
   send_btn.click()
   
   current_text = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tcarpentier.myAndroidApp:id/textView")')
   assert current_text.text == "It's a trap!"

   driver.back()
   
   # teardown appium
   driver.quit()