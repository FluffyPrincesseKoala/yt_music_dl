# YouTube Audio Downloader

A Python script that downloads audio tracks from YouTube using yt-dlp.

## Features
- Downloads audio in best available quality
- Supports custom input files and output directories
- Skips comments and empty lines in track lists
- Progress tracking with download counters
- Error handling for failed downloads

## Requirements
- Python 3.6+
- yt-dlp (Windows executable included in same directory)

## Installation
1. Place `yt-dlp.exe` in the same directory as the script
2. Install Python dependencies:
   ```cmd
   pip install argparse
   ```

## Usage
```
python download_music.py [-h] [-i INPUT] [-o OUTPUT]
```

### Arguments
| Argument | Description                          | Default          |
|----------|--------------------------------------|------------------|
| `-h`     | Show help message                    |                  |
| `-i`     | Input text file with track list      | `tracks.txt`     |
| `-o`     | Output directory for downloads       | `Music Downloads`|

### Input File Format
Create a text file with one track per line:
```
Artist - Track Name
Another Artist - Another Track
# This is a comment (will be ignored)
```

## Example
1. Create `my_tracks.txt`:
   ```
   Daft Punk - Around the World
   The Chemical Brothers - Galvanize
   ```

2. Run download:
   ```cmd
   python download_music.py -i my_tracks.txt -o "My Music"
   ```

3. Output:
   ```
   Found 2 tracks to download
   Input file: C:\path\to\my_tracks.txt
   Output directory: C:\path\to\My Music

   (1/2) Downloading: Daft Punk - Around the World
   (2/2) Downloading: The Chemical Brothers - Galvanize

   Download complete! Files saved in: C:\path\to\My Music
   ```

## Output Files
Files will be saved as:
```
[output_dir]/[track title].ext
```
(e.g., `Music Downloads/Daft Punk - Around the World.m4a`)

## Notes
- Requires `yt-dlp.exe` in the same directory
- On first run, may need to allow through Windows Defender
- For large lists, consider adding delays between downloads
```

### Key Points Included:
1. Clear usage instructions for Windows users
2. Emphasis on the yt-dlp.exe requirement
3. Simple input file format example
4. Argument documentation in table format
5. Expected output structure
6. Basic troubleshooting notes

Would you like me to add any additional sections like:
- Error handling details?
- Batch file wrapper example?
- Scheduled task configuration?
- Alternative audio format options?