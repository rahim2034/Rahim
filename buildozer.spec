[app]

title = Privacy Shield
package.name = privacyshield
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

version = 1.0
orientation = portrait

android.permissions = INTERNET

requirements = python3,kivy

android.api = 35
android.minapi = 21
android.arch = arm64-v8a

fullscreen = 0
log_level = 2


[buildozer]

build_dir = .buildozer
bin_dir = bin
log_level = 2
