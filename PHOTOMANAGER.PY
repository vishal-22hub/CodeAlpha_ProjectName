import os
import shutil

def organize_photos(source_dir, dest_dir):
    # Create destination folder if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created directory: {dest_dir}")

    # Counter for moved files
    count = 0

    # Iterate through files in the source directory
    for filename in os.listdir(source_dir):
        # Check for .jpg extension (case-insensitive)
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)

            # Move the file
            shutil.move(source_path, dest_path)
            print(f"Moved: {filename}")
            count += 1

    print(f"\nTask Complete! Total files moved: {count}")

# Example Usage:
# Replace these paths with your actual folder locations
source = "./Downloads" 
destination = "./My_Jpg_Photos"

organize_photos(source, destination)