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

# 🔥 FORCE STABLE BUILD TOOLS (BLOCKS 37 ISSUE)
android.build_tools_version = 34.0.0

android.ndk = 25b
android.archs = arm64-v8a

android.permissions = INTERNET
android.enable_androidx = True

# 🔥 IMPORTANT STABILITY FLAG
p4a.branch = master

# keep icon OFF until build works
# icon.filename = Path_Icon.png

[buildozer]
log_level = 2
warn_on_root = 0
