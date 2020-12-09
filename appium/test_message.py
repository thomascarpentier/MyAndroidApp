# -*- coding: utf-8 -*-
import pytest
from appium import webdriver


class TestDemoApp:

    @pytest.mark.parametrize("message", [
        "This is a demo",
        "Genymotion PaaS",
        "Search @genymotion on twitter",
        "Text with numbers : 02015453321",
    ])
    def test_send_message(self, message, getAPKPath):


        capabilities = {
            "platformName": "Android",
            "deviceName": "Genymotion PaaS Device",
            "app": getAPKPath,
            "automationName": "UiAutomator2",
            "noReset": True,
        }
        url = "http://localhost:4723/wd/hub"
        driver = webdriver.Remote(url, capabilities)

        txt_ipt = driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.tcarpentier.myAndroidApp:id/editText")'
        )
        txt_ipt.clear()
        txt_ipt.send_keys(message)

        send_btn = driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.tcarpentier.myAndroidApp:id/button")'
        )
        send_btn.click()

        current_text = driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.tcarpentier.myAndroidApp:id/textView")'
        )
        assert current_text.text == message

        driver.back()

        # teardown appium
        driver.quit()
