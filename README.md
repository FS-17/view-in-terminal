# Image to Terminal

This Python project converts images or videos to ASCII art and displays them in the terminal.

## Files

- [viewInTerminal.py](viewInTerminal.py): The main script that handles image and video processing.
- [helper.py](helper.py): Contains helper functions for validating input and resizing the terminal.
- [map.json](map.json): A mapping file used for converting pixel values to ASCII characters.

## Usage

Run the `viewInTerminal.py` script with the following arguments:

- `src`: The source image or video file. Example: `path/to/image.jpg`
- `-c`, `--color`: (Optional) The number of colors to use in the image. Default is 45. Example: `20`

Example command:

```sh
python viewInTerminal.py path/to/image.jpg -c 20
```