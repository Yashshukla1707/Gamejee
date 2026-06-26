[app]

title = Path

package.name = pathgame

package.domain = org.shivansh


source.dir = .


source.include_exts = py,png,jpg,jpeg,gif,wav,mp3,ttf,json,kv


version = 1.2


requirements = python3==3.11.9,kivy


orientation = landscape


fullscreen = 0


android.api = 33

android.minapi = 21

android.ndk = 25b


android.archs = arm64-v8a


android.python_version = 3.11


android.accept_sdk_license = True


android.enable_androidx = True


android.permissions = INTERNET


p4a.bootstrap = sdl2


[buildozer]

log_level = 2

warn_on_root = 0
