#h5ai Connector for Kodi
A simple, lightweight Kodi video addon that allows you to browse and play media from web server directories, specifically tailored for sites using h5ai, but generic enough to work with many standard Apache-style directory listings.

This plugin lets you add multiple web directories as sources and navigate them directly within the Kodi interface.

Features
Multiple Sources: Configure up to 10 different web directory sources.

Simple Navigation: Browse remote directories just like a local file system.

Direct Playback: Play video files directly from the source.

Lightweight: No complex dependencies or background services.

Broad Compatibility: Works with h5ai and many other common web directory listing formats.

Prerequisites
Kodi version 18 (Leia) or newer.

Installation Instructions
You can install this addon by downloading the latest release .zip file from the repository.

Go to the Releases page of this GitHub repository.

Download the plugin.video.h5ai.zip file from the latest release.

Open Kodi.

Navigate to Settings (the gear icon).

Go to System.

Select the Add-ons tab on the left.

Make sure the Unknown sources option is enabled. You will see a warning; please accept it.

Navigate back to the Settings -> Add-ons menu.

Select Install from zip file.

Locate the plugin.video.h5ai.zip file you downloaded earlier and select it.

Wait for the notification in the top-right corner that says "h5ai Connector Add-on installed".

Configuration
Before you can use the addon, you need to add at least one source URL.

Navigate to the Add-ons section in Kodi's main menu.

Go to Video add-ons.

Find the h5ai Connector addon, and open its context menu:

Mouse/Keyboard: Right-click on the icon.

Remote/Controller: Press the menu button.

Touchscreen: Long-press the icon.

Select Settings.

In the settings window, you will see fields for Source 1 Name, Source 1 URL, and so on.

Source Name: A friendly name for the directory (e.g., "Animation Movies", "FTP Server 5").

Source URL: The full URL to the web directory you want to browse. Make sure it ends with a /.

Fill in the details for as many sources as you need.

Click OK to save the settings.

How to Use
Once installed and configured, using the addon is straightforward:

Go to the Add-ons section from the Kodi main menu.

Select Video add-ons.

Click on h5ai Connector.

You will see the list of sources you configured. Select one to start browsing its files and folders.

Troubleshooting
"h5ai Connector Error: Check the log for more information"
This is a generic error. To find the actual cause, you need to check the main Kodi log file.

Location of kodi.log:

Windows: %APPDATA%\Kodi\kodi.log

Android: /sdcard/Android/data/org.xbmc.kodi/files/.kodi/temp/kodi.log

Linux: ~/.kodi/temp/kodi.log

macOS: /Users/<your_user_name>/Library/Application Support/Kodi/temp/kodi.log

Open the log file and look for lines containing [h5ai Connector] to find the specific error message.

The addon opens but the directory is empty.
This usually means one of two things:

The URL you entered in the settings is incorrect or not accessible. Double-check it in a web browser.

The web page's HTML structure is too different from a standard directory listing for the addon to parse.

Contributing
Contributions are welcome! If you have an idea for a new feature or have found a bug, please open an issue to discuss it.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.
