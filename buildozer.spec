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

# 🔥 ANDROID CONFIG (LOCKED STABLE VERSION)
android.api = 34
android.minapi = 21

# 🚨 CRITICAL FIX: stops Build-Tools 37 forever
android.build_tools_version = 34.0.0

android.ndk = 25b
android.archs = arm64-v8a

android.permissions = INTERNET
android.enable_androidx = True

# 🔥 prevents broken builds
p4a.branch = master

# icon disabled until success
# icon.filename = Path_Icon.png

[buildozer]
log_level = 2
warn_on_root = 0
