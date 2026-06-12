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

# Android stable config (THIS IS IMPORTANT)
android.api = 33
android.minapi = 21
android.ndk = 27b

# DO NOT FORCE BUILD TOOLS (THIS WAS YOUR MAIN ERROR)
# android.build_tools = 37.0.0   <-- REMOVE IF YOU SEE IT

android.archs = arm64-v8a, armeabi-v7a

# prevents auto-breaking updates
android.skip_update = True

log_level = 2
