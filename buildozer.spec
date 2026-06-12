[app]
title = Gamejee
package.name = gamejee
package.domain = org.gamejee

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

# IMPORTANT: reduce random build issues
log_level = 2

[buildozer]

# Force stable Android API (VERY IMPORTANT)
android.api = 33
android.minapi = 21
android.ndk = 25b

# Avoid broken latest tools
android.sdk = 33
android.ndk_path =

# Force non-interactive installs (fixes your "Accept? y/N")
android.accept_sdk_license = True

# Force correct build tools (fix AIDL issue)
android.sdk_build_tools = 33.0.2

# Architecture (stable)
android.arch = arm64-v8a

# Avoid problematic updates
warn_on_root = 0

# Prevent interactive prompts
log_level = 2

# Packaging mode
p4a.branch = stable
