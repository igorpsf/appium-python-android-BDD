from appium import webdriver

# Android (Real device)
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "8",
    "deviceName": "70c124cb",
    "app": "/Users/igor/Desktop/Docs/Git/Python/appium-python-android-BDD/app_binaries/original.apk",
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
