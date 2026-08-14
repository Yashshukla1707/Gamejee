[app]

title = Path

package.name = pathgame3d

package.domain = org.shivansh


source.dir = .


source.include_exts = py,png,jpg,jpeg,gif,wav,mp3,ttf , obj , mtl,json,kv


source.include_patterns = Images/*


version = 1.0


requirements = python3,kivy


orientation = landscape


fullscreen = 0


icon.filename = Images/Path_Icon.jpg
android.splash_color = #000000


android.api = 34

android.minapi = 21

android.ndk = 25b


android.archs = arm64-v8a


android.accept_sdk_license = True


android.enable_androidx = True


android.permissions = INTERNET


p4a.bootstrap = sdl2



[buildozer]

log_level = 2

warn_on_root = 0
