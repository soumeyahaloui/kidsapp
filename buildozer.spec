[app]

title = My Application
package.name = myapp
package.domain = org.test
source.dir = src
source.include_exts = py,png,jpg,kv,atlas,mp3
source.include_patterns = assets/*.png, assets/*.jpg, assets/audio/ar/*.mp3, assets/audio/fr/*.mp3
version = 0.1
requirements = python3==3.10.0, kivy, requests
icon.filename = assets/images/icon/appkidicon.png
orientation = portrait
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
debug = 1
android.api = 31
android.minapi = 21
android.ndk = 21e
android.ndk_path = /home/hadeel/.buildozer/android/platform/android-ndk-r25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
p4a.bootstrap = sdl2
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false
log_level = 2
warn_on_root = 1
