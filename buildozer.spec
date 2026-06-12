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

[android]

android.api = 33
android.minapi = 21
android.arch = arm64-v8a

# IMPORTANT: prevents broken SDK auto-pull issues
p4a.branch = master
