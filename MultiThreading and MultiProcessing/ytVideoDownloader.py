import os
from pytubefix import YouTube
from pytubefix.cli import on_progress
from concurrent.futures import ThreadPoolExecutor
from urllib.error import URLError
import time


def download_video(url, output_path='./downloads'):
    """
    Download a YouTube video in the highest resolution available.

    Args:
        url (str): YouTube video URL
        output_path (str): Directory to save the video
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)

        # Create YouTube object
        yt = YouTube(url, on_progress_callback = on_progress)


        # Get the highest resolution stream (progressive if available, else adaptive)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not video:
            video = yt.streams.filter(adaptive=True, file_extension='mp4').order_by('resolution').desc().first()

        if not video:
            print(f"No suitable video stream found for: {url}")
            return

        print(f"Downloading: {yt.title} ({video.resolution})...")
        start_time = time.time()

        # Download the video
        video.download(output_path)

        download_time = time.time() - start_time
        print(f"Finished downloading: {yt.title} ({download_time:.2f} seconds)")

    except URLError as e:
        print(f"Connection error while downloading {url}: {e}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


def download_multiple_videos(urls, max_workers=4):
    """
    Download multiple YouTube videos using multi-threading.

    Args:
        urls (list): List of YouTube video URLs
        max_workers (int): Number of concurrent downloads
    """
    print(f"Starting download of {len(urls)} videos with {max_workers} threads...")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(download_video, urls)

    print("All downloads completed!")


if __name__ == "__main__":
    # Example usage:
    video_urls = [
        "https://youtu.be/dkKKHlbltDQ?si=Hj8afDt2jEZJh-_N",
        "https://youtu.be/rSmbLLTHRBc?si=-rPOm7hXYF8AEGlt",
        "https://youtu.be/IoDfncWoRy8?si=6rwMRZkKi7A_3j52",
        "https://youtu.be/QvigW9_NR-o?si=3miIYQVJ4AHC_OFu"
        # Add more URLs here
    ]

    # Replace with your actual video URLs
    # video_urls = []  # You'll provide these

    download_multiple_videos(video_urls)