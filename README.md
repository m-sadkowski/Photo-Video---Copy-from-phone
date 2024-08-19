# Photo and Video Extractor

## Overview

This Python script allows users to search through a directory for image and video files, and then copies these files to a specified destination folder. The copied files are renamed based on their last modification date to help organize them.

## Features

- **Search Functionality:** Walks through the selected directory to find image and video files.
- **File Support:** Handles a range of common image and video file formats.
- **Date-based Naming:** Renames copied files using their last modification date to avoid name conflicts and ensure chronological organization.

## Prerequisites

- Python 3.x
- `tkinter` (usually included with Python's standard library)

## Installation

Clone this repository and ensure you have Python 3 installed on your system.

```bash
git clone https://github.com/yourusername/photo-video-extractor.git
cd photo-video-extractor
```

## Usage

1. **Run the Script:**

   Execute the script using Python:

   ```bash
   python photo_video_extractor.py
   ```

2. **Select Folders:**

   - **Input Folder:** Choose the folder containing the files you want to extract.
   - **Destination Folder:** Choose the folder where the extracted files will be copied.

3. **Operation:**

   The script will search through the input folder, identify image and video files, and copy them to the destination folder with new names based on their last modification date.

## Code Details

### Supported File Extensions

The script supports the following image and video file extensions:

- **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.tif`, `.svg`, `.ico`
- **Videos:** `.mp4`, `.mov`, `.wmv`, `.avi`, `.mkv`, `.flv`, `.webm`, `.vob`, `.ogv`, `.ogg`, `.drc`, `.mng`, `.qt`, `.mpg`, `.mpeg`, `.3gp`

### Functions

- `wybierz_folder()`: Opens a dialog to select a directory.
- `przeszukaj_folder(wejsciowy_folder, docelowy_folder)`: Searches for supported files in the input folder and copies them to the destination folder with renamed based on their modification date.

## Example Output

```
Wybrano folder do przeszukania: C:/Users/YourUser/Pictures
Wybrano folder docelowy: C:/Users/YourUser/Extracted
Skopiowano: C:/Users/YourUser/Pictures/photo1.jpg do C:/Users/YourUser/Extracted/2024-08-18_12-30-00.jpg
Skopiowano: C:/Users/YourUser/Pictures/video1.mp4 do C:/Users/YourUser/Extracted/2024-08-18_13-45-00.mp4
Operacja zakończona.
```

## Notes

- Ensure that the destination folder is empty or contains files that won't conflict with the names generated.
- The script assumes you have necessary permissions to read and write files in the selected directories.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues and pull requests to improve the functionality or fix bugs.

## Contact

For any questions or support, please contact [msadkowski000@gmail.com](mailto:msadkowski000@gmail.com).
