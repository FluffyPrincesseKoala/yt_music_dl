import os
import subprocess
import argparse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Download audio tracks from YouTube')
    parser.add_argument('-i', '--input', default='tracks.txt', help='Input file containing track list (default: tracks.txt)')
    parser.add_argument('-o', '--output', default='Music Downloads', help='Output directory for downloads (default: Music Downloads)')
    args = parser.parse_args()

    # Create output directory if it doesn't exist
    os.makedirs(args.output, exist_ok=True)

    # Read tracks from file, ignoring empty lines and comments
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            tracks = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print(f"Error: Input file '{args.input}' not found!")
        exit(1)

    print(f"Found {len(tracks)} tracks to download")
    print(f"Input file: {os.path.abspath(args.input)}")
    print(f"Output directory: {os.path.abspath(args.output)}\n")

    # Download loop
    for index, track in enumerate(tracks, 1):
        print(f"({index}/{len(tracks)}) Downloading: {track}")
        
        try:
            result = subprocess.run(
                [
                    "yt-dlp",
                    "--extract-audio",
                    "--audio-format", "best",
                    "--audio-quality", "0",
                    "--output",
                    os.path.join(args.output, "%(title)s.%(ext)s"),
                    "--no-playlist",
                    "--quiet",
                    "--no-warnings",
                    f"ytsearch1:{track}"
                ],
                capture_output=True,
                text=True,
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {track}:")
            print(e.stderr if e.stderr else "Unknown error")
            continue
        except Exception as e:
            print(f"Unexpected error with {track}: {str(e)}")
            continue

    print("\nDownload complete! Files saved in:", os.path.abspath(args.output))

if __name__ == "__main__":
    main()