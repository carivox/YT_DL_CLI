# YouTube Downloader CLI

Ein einfacher und übersichtlicher **YouTube Downloader für die Kommandozeile**, entwickelt in Python. Das Programm nutzt [yt-dlp](https://github.com/yt-dlp/yt-dlp), um Videos oder Audios von YouTube herunterzuladen und automatisch im lokalen Download-Ordner zu speichern.

## Funktionen

* 🎬 Download von YouTube-Videos als **MP4**
* 🎵 Download von Audios als **MP3**
* 🔊 Download von Audios als **WAV**
* 🎧 Download von Audios als **FLAC**
* 📁 Automatische Speicherung im Benutzerordner `Downloads`
* 💻 Einfache Bedienung über die Kommandozeile
* ⚙️ Automatische Verarbeitung der heruntergeladenen Audiodateien über FFmpeg
* 🐍 Umsetzung vollständig in Python

## Verfügbare Formate

| Auswahl | Format | Beschreibung                    |
| ------- | ------ | ------------------------------- |
| `1`     | MP4    | Video inklusive Audio           |
| `2`     | MP3    | Audio mit 192 kbit/s            |
| `3`     | WAV    | Unkomprimiertes Audio           |
| `4`     | FLAC   | Verlustfrei komprimiertes Audio |

## Voraussetzungen

* Python 3
* `yt-dlp`
* FFmpeg

Die benötigten Python-Abhängigkeiten können beispielsweise mit folgendem Befehl installiert werden:

```bash
pip install yt-dlp
```

Für die Konvertierung von Audioformaten wird außerdem **FFmpeg** benötigt.

## Verwendung

Das Programm wird über die Kommandozeile gestartet:

```bash
python main.py
```

Anschließend wird zunächst nach einem YouTube-Link gefragt. Danach kann das gewünschte Ausgabeformat ausgewählt werden.

Beispiel:

```text
╔═══════════════════════════════╗
║     YouTube Downloader CLI    ║
╚═══════════════════════════════╝

Bitte füge den YouTube-Link ein: https://www.youtube.com/watch?v=...

Verfügbare Formate:
[1] MP4 (Video)
[2] MP3 (Audio)
[3] WAV (Audio verlustfrei)
[4] FLAC (Audio verlustfrei komprimiert)

Bitte wähle ein Format (1-4):
```

Nach erfolgreichem Download wird die Datei automatisch im lokalen Downloads-Ordner abgelegt.

## Technischer Aufbau

Das Projekt besteht aus wenigen klar getrennten Funktionen:

* `get_download_path()` bestimmt den lokalen Download-Ordner.
* `get_ydl_opts()` erstellt abhängig vom gewählten Format die passenden `yt-dlp`-Optionen.
* `main()` übernimmt die Benutzerinteraktion, Validierung der Eingaben und Durchführung des Downloads.

Für die Audioformate MP3, WAV und FLAC werden die heruntergeladenen Audiodateien anschließend über die FFmpeg-Postprozessoren von `yt-dlp` konvertiert.
