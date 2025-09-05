# h5ai Connector for Kodi

*A Kodi Add-On for browsing and playing videos from web server directories.*

---

## Installation & Configuration

### 1. Install the Add-on

1. Navigate to `Settings -> System -> Add-ons` and enable **Unknown sources**.
2. Navigate back to `Settings -> Add-ons` and select **Install from zip file**.
3. Locate and select the `plugin.video.h5ai.zip` file.

### 2. Configure the Sources

1. Navigate to `Add-ons -> Video add-ons`.
2. Open the context menu for **h5ai Connector** and select **Settings**.
3. Enter a **Name** and **URL** for each source you wish to add.
4. Click **OK** to save.

---

## How It Works

The add-on parses the HTML of a web directory to find links to files and folders. It is designed to be generic but also filters out common clutter from h5ai installations.

### Example Directory Parsing

| Original Server Listing        | What You See in Kodi   |
|-------------------------------|-------------------------|
| Movie A (2024)/               | Movie A (2024)          |
| TV Show (2023)/               | TV Show (2023)          |
| powered by h5ai               | *(hidden)*              |
| modern browsers               | *(hidden)*              |

---

## Troubleshooting

If you encounter an error, the best way to diagnose the problem is by checking the main Kodi log file.

### Common Log Locations

| Operating System | Path to `kodi.log` |
|------------------|--------------------|
| Windows          | `%APPDATA%\Kodi\kodi.log` |
| Android          | `/sdcard/Android/data/org.xbmc.kodi/files/.kodi/temp/kodi.log` |
| Linux            | `~/.kodi/temp/kodi.log` |
| macOS            | `/Users/USER_NAME/Library/Application Support/Kodi/temp/kodi.log` |

---

## Contributing

Contributions are welcome! Please open an issue to discuss any bugs or feature requests.

---

## License

This project is licensed under the **MIT License**.
