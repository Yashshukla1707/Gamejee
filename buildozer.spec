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

# ----------------------------
# ANDROID STABLE CONFIG
# ----------------------------

android.api = 33
android.minapi = 21

# VERY IMPORTANT (prevents broken NDK installs)
android.ndk = 25b

# FORCE stable architecture
android.arch = arm64-v8a

# FIX: prevents Android 36/37 chaos
android.sdk_build_tools = 33.0.2

# STOP auto-updating broken SDK
android.skip_update = True

# AUTO ACCEPT LICENSES (FIXES YOUR PROMPT ERROR)
android.accept_sdk_license = True

# ICON (safe - remove if file missing)
icon.filename = icon.png

# DEBUG (helps if future error happens)
log_level = 2
