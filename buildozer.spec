[app]
title = Gamejee
package.name = gamejee
package.domain = org.game

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

log_level = 2

[buildozer]

# 🔥 LOCK STABLE ANDROID VERSION (VERY IMPORTANT)
android.api = 33
android.minapi = 21

# 🔥 Stable NDK (prevents random crashes)
android.ndk = 25b

# 🔥 Force architecture (prevents emulator junk builds)
android.arch = arm64-v8a

# 🔥 Prevent random updates breaking builds
warn_on_root = 0
