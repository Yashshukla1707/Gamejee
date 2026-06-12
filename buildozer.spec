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

# 🔥 FORCE STABLE ANDROID STACK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a

# 🔥 CRITICAL: STOP ANDROID 36/37 BUILD TOOLS
android.sdk_build_tools = 33.0.2

android.skip_update = True
android.accept_sdk_license = True

# REMOVE THIS IF FILE MISSING
# icon.filename = icon.png

log_level = 2
warn_on_root = 1
