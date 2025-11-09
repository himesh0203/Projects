import os
import shutil
from pathlib import Path

def organize_downloads_folder(downloads_path):
    """
    Organizes files in the specified downloads folder into subfolders based on file extensions.
    """
    downloads_dir = Path(downloads_path)

    # Define categories for file types
    file_categories = {
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Executables": [".exe", ".msi", ".dmg", ".app"],
        "Spreadsheets": [".xls", ".xlsx", ".csv"],
        "Presentations": [".ppt", ".pptx"],
        "Scripts": [".py", ".sh", ".bat", ".js", ".html", ".css"]
    }

    # Create destination folders if they don't exist
    for category in file_categories:
        (downloads_dir / category).mkdir(parents=True, exist_ok=True)
    (downloads_dir / "Others").mkdir(parents=True, exist_ok=True)

    # Iterate through files and move them
    for item in downloads_dir.iterdir():
        if item.is_file():
            file_extension = item.suffix.lower()
            moved = False
            for category, extensions in file_categories.items():
                if file_extension in extensions:
                    shutil.move(item, downloads_dir / category / item.name)
                    moved = True
                    break
            if not moved:
                shutil.move(item, downloads_dir / "Others" / item.name)

    print(f"Downloads folder '{downloads_path}' organized successfully!")

if __name__ == "__main__":
    # Specify your Downloads folder path here
    # Example for Windows: "C:/Users/YourUsername/Downloads"
    # Example for macOS/Linux: "/Users/YourUsername/Downloads"
    # You can also use Path.home() / "Downloads" for a cross-platform approach
    
    # Replace with your actual downloads path or use the automated method
    my_downloads_folder = str(Path.home() / "Downloads") 
    
    organize_downloads_folder(my_downloads_folder)
