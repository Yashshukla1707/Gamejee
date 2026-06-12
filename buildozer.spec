[app]
title = MyGame
package.name = mygame
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy==2.3.0

orientation = portrait

fullscreen = 1

android.api = 34
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a

android.allow_backup = True

log_level = 2

# IMPORTANT: avoids build-tools auto chaos
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
