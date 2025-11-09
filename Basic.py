import os
import shutil
from pathlib import Path

def organize_downloads_folder(downloads_path):
    """
    Organizes files in the specified Downloads folder into subfolders based on file extensions.
    """
    downloads_dir = Path(downloads_path)

    if not downloads_dir.is_dir():
        print(f"Error: '{downloads_path}' is not a valid directory.")
        return

    # Define common file types and their corresponding folder names
    file_type_mapping = {
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Executables": [".exe", ".msi", ".dmg", ".app"],
        "Spreadsheets": [".xls", ".xlsx", ".csv"],
        "Presentations": [".ppt", ".pptx"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".sh"]
    }

    # Create destination folders if they don't exist
    for folder_name in file_type_mapping.keys():
        dest_folder = downloads_dir / folder_name
        dest_folder.mkdir(exist_ok=True)

    # Process each item in the downloads folder
    for item in downloads_dir.iterdir():
        if item.is_file():
            file_extension = item.suffix.lower()
            moved = False
            for folder, extensions in file_type_mapping.items():
                if file_extension in extensions:
                    destination_folder = downloads_dir / folder
                    try:
                        shutil.move(str(item), str(destination_folder / item.name))
                        print(f"Moved '{item.name}' to '{folder}'")
                        moved = True
                        break
                    except shutil.Error as e:
                        print(f"Error moving '{item.name}': {e}")
                        moved = True # Prevent moving to 'Others' if there was a specific error
                        break
            
            if not moved:
                # Move unclassified files to an 'Others' folder
                others_folder = downloads_dir / "Others"
                others_folder.mkdir(exist_ok=True)
                try:
                    shutil.move(str(item), str(others_folder / item.name))
                    print(f"Moved '{item.name}' to 'Others'")
                except shutil.Error as e:
                    print(f"Error moving '{item.name}' to 'Others': {e}")

    print("\nDownloads folder organization complete!")

if __name__ == "__main__":
    # Specify your Downloads folder path here
    # Example for Windows: r"C:\Users\YourUsername\Downloads"
    # Example for macOS/Linux: "/Users/YourUsername/Downloads"
    # Using Path.home() / "Downloads" is generally more platform-independent
    downloads_folder_path = Path.home() / "Downloads" 
    
    organize_downloads_folder(downloads_folder_path)
