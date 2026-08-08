[app]

title = Ataques Espaciales
package.name = ataquesespaciales
package.domain = org.ataquesespaciales

source.dir = .
source.include_exts = py,png,jpg,jpeg,json,wav,mp3,ogg

version = 1.0

requirements = python3,pygame==2.5.2,jnius,sdl2,sdl2_image,sdl2_mixer,sdl2_ttf

orientation = portrait
fullscreen = 1

android.permissions = VIBRATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a,armeabi-v7a

[buildozer]
log_level = 2

