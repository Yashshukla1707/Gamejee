[app]
title = Gamejee
package.name = gamejee
package.domain = org.yourname

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21

# VERY IMPORTANT FIX
android.ndk = 27b

# DO NOT FORCE ANY BUILD TOOLS
# android.build_tools = MUST NOT EXIST ANYWHERE

android.archs = arm64-v8a, armeabi-v7a
android.skip_update = True

log_level = 2
