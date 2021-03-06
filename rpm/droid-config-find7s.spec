# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc

%define device find7s
%define vendor oppo

%define vendor_pretty OPPO
%define device_pretty Find7s

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 2.7

# We assume most devices will
%define have_modem 1

# Community HW adaptations need this
%define community_adaptation 1

Provides: ofono-configs

%include droid-configs-device/droid-configs.inc
