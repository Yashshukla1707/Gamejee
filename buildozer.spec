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

# --- ICON (SAFE OPTION) ---
# If icon.png causes issues, you can comment it out
# icon.filename = icon.png

# --- ANDROID SETTINGS (IMPORTANT FIXES) ---
android.api = 33
android.minapi = 21

# FIX: stable NDK (your crash was from r28c download failure)
android.ndk = 27b

# FIX: stable architectures (prevents build failures)
android.archs = arm64-v8a, armeabi-v7a

# FIX: avoids build confusion in CI
android.skip_update = True

# --- DEBUG / LOGGING ---
log_level = 2
warn_on_root = 0

# --- OPTIONAL STABILITY FLAGS ---
android.private_storage = True
android.allow_backup = True
