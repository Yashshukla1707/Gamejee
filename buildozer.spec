[app]

title = MyGame

package.name = mygame

package.domain = org.example


source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,gif,wav,mp3,ttf,json,atlas


version = 1.1


requirements = python3,kivy


# Force whole app to landscape
orientation = landscape

fullscreen = 1


android.api = 34

android.minapi = 21

android.ndk = 25b


android.arch = arm64-v8a


android.accept_sdk_license = True


[buildozer]

log_level = 1

warn_on_root = 0
