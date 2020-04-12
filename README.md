### Install packages:
1. Selenium
2. Appium-Python-Client
3. Behave

### Android (Real device) | Need to change all capabilities

desired_capabilities = {

    "platformName": "Android",
    "platformVersion": "8",
    "deviceName": "***",
    "app": "/Users/igor/Desktop/Docs/Git/Python/appium-python-android-BDD/app_binaries/original.apk",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
