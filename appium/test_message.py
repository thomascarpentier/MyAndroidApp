# -*- coding: utf-8 -*-
import pytest
from appium import webdriver


class TestDemoApp:
    @pytest.fixture(scope="module")
    def appium(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Genymotion Cloud SaaS Devices",
            "app": getAPKPath,
            "automationName": "UiAutomator2",
            "noReset": True,
        }
        url = "http://localhost:4723/wd/hub"
        appium_ = webdriver.Remote(url, desired_caps)

        yield appium_
        # teardown appium
        appium_.quit()



    @pytest.mark.parametrize("message", [
        "This is a demo",
        "Genymotion PaaS",
        "Search @genymotion on twitter",
        "Text with numbers : 02015453321",
    ])
    def test_send_message(self, appium, message):

        self.driver = appium
        txt_ipt = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.tcarpentier.myAndroidApp:id/editText")'
        )
        txt_ipt.clear()
        txt_ipt.send_keys(message)

        send_btn = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.tcarpentier.myAndroidApp:id/button")'
        )
        send_btn.click()

        current_text = self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.tcarpentier.myAndroidApp:id/textView")'
        )
        assert current_text.text == message

        self.driver.back()
