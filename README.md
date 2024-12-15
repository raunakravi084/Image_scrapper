# Google Images Scraper

This Python script uses Selenium to scrape images from Google Images based on a search query. It downloads the images to a specified directory.

## Features

- Scrapes images from Google Images.
- Downloads images to a local directory.
- Supports headless mode for running in the background.

## Prerequisites

- Python 3.6 or higher
- Selenium
- Chrome WebDriver

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/google-images-scraper.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the appropriate version of Chrome WebDriver and place it in your system's PATH.

## Usage

1. Run the script:
   ```bash
   python Scraper.py
   ```

2. The script will prompt you to enter a search query and the number of images to download.

## Example

To download 10 images of "cars":
```bash
python Scraper.py
```

## Notes

- The script creates a directory named `downloaded_images` in the current working directory to store the downloaded images.
- The script uses headless mode by default, so it runs without opening a browser window.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
