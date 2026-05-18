# Image Auto-Converter

Image Auto-Converter is a Python-based tool designed to automate the conversion of images between different formats. It provides a simple and flexible way to batch convert your image files with minimal effort.

## Features

- Batch convert images to multiple formats (e.g., JPG, PNG, BMP, TIFF, etc.)
- Command-line interface for ease of use
- Customizable output directory and file naming
- Support for common image formats
- Simple installation and usage

## Installation

Clone this repository and install the required dependencies:

```bash
git clone https://github.com/Pedro-Rosa007/Image_Auto-Converter.git
cd Image_Auto-Converter
pip install -r requirements.txt
```

## Usage

Basic usage example:

```bash
python image_converter.py --input /path/to/images --output /path/to/converted --format png
```

### Command-line Options

- `--input`: Directory containing images to convert (required)
- `--output`: Directory to save converted images (optional, default: `converted_images`)
- `--format`: Target image format, e.g., jpg, png, bmp (required)
- `--quality`: (Optional) Output quality for lossy formats

## Requirements

- Python 3.x
- Pillow (or other dependencies specified in `requirements.txt`)

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
