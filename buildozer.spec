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

# IMPORTANT FIXES
android.api = 34
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a

# FORCE STABLE BUILD TOOLS (THIS FIXES YOUR ERROR)
android.sdk_build_tools = 34.0.0

# Prevent random SDK failures
android.skip_update = True

# ICON (safe option)
# If icon.png exists → keep it
# If NOT → comment this line
icon.filename = icon.png

# Avoid license / interactive prompts
android.accept_sdk_license = True
