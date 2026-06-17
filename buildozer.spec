[app]
title = Path
package.name = mygame
package.domain = org.example

icon.filename = Images/Path_Icon.png

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.api = 34
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a

android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
