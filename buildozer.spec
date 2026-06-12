[app]
title = MyGame
package.name = mygame
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 1

# IMPORTANT STABLE ANDROID SETTINGS
android.api = 34
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a

# FORCE NO INTERACTIVE PROMPTS
android.accept_sdk_license = True
android.gradle_dependencies =

# Reduce build noise + speed
log_level = 1
warn_on_root = 0

[buildozer]
log_level = 1
