# frogger-infinite
Building my first game in pygame

# Setup
Install [butler](https://itch.io/docs/butler/installing.html) for pushing releases to itch.io

# Releasing new build
1. Build executable
    1.  `python setup.py bdist_mac --iconfile assets/frogger_icon.icns --bundle-name FroggerInfinite`
2. Push build to itch.io
    1. `butler push build/FroggerInfinite.app drawacard/frogger-infinite:osx-beta`
