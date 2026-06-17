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

# IMPORTANT: DO NOT force build-tools (let p4a handle it safely)
# REMOVE THIS LINE COMPLETELY:
# android.build_tools_version = 34.0.0

android.ndk = 25b
android.archs = arm64-v8a

android.permissions = INTERNET
android.enable_androidx = True

p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 0warn_on_root = 0
