[app]
title = Path
package.name = mygame
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

android.permissions = INTERNET
android.enable_androidx = True

# IMPORTANT: DO NOT use icon for now (we fixed your crash)
# icon.filename = Path_Icon.png

[buildozer]
log_level = 2
warn_on_root = 0
