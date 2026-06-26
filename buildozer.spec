Buildozer.spec

[app]

title = Path

package.name = pathgame

package.domain = org.shivansh
[app]

# Your existing settings stay here

# Android crash fixes
android.disable_multitouch = 1
android.private_storage = True
android.add_src = .


source.dir = .


source.include_exts = py,png,jpg,jpeg,gif,wav,mp3,ttf,json


version = 1.1


requirements = python3,kivy


orientation = landscape


fullscreen = 0


android.api = 33

android.minapi = 21

android.ndk = 25b


android.archs = arm64-v8a,armeabi-v7a


android.accept_sdk_license = True


android.enable_androidx = True


android.permissions = INTERNET


[buildozer]

log_level = 2

warn_on_root = 1
