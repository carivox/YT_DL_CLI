import os
from pathlib import Path
from yt_dlp import YoutubeDL

def get_download_path() -> Path:
    return Path.home() / "Downloads"

def get_ydl_opts(choice: str, download_dir: Path) -> dict:
    outtmpl = str(download_dir / "%(title)s.%(ext)s")

    opts = {
        "outtmpl": outtmpl,
        "quiet": False,
        "no_warnings": True,
    }

    if choice == "1":
        opts["format"] = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
    elif choice == "2":
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ]
    elif choice == "3":
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [
            {"key": "FFmpegExtractAudio", "preferredcodec": "wav"}
        ]
    elif choice == "4":
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [
            {"key": "FFmpegExtractAudio", "preferredcodec": "flac"}
        ]

    return opts


def main():
    print()
    print("╔═══════════════════════════════╗")
    print("║     YouTube Downloader CLI    ║")
    print("╚═══════════════════════════════╝")
    print()

    url = input("Bitte füge den YouTube-Link ein: ").strip()
    if not url:
        print("Fehler: Kein Link eingegeben.")
        return

    print("\nVerfügbare Formate:")
    print("[1] MP4 (Video)")
    print("[2] MP3 (Audio)")
    print("[3] WAV (Audio verlustfrei)")
    print("[4] FLAC (Audio verlustfrei komprimiert)")

    choice = input("Bitte wähle ein Format (1-4): ").strip()

    if choice not in ["1", "2", "3", "4"]:
        print("Ungültige Auswahl.")
        return

    download_dir = get_download_path()
    ydl_opts = get_ydl_opts(choice, download_dir)

    print("\nStarte Download... Bitte warten...")

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\nErfolgreich im Download-Ordner gespeichert!")
    except Exception as e:
        print(f"\nEin Fehler ist aufgetreten: {e}")

    print("\n-----------------------------------")
    input("Drücke ENTER, um das Fenster zu schließen...")


if __name__ == "__main__":
    main()