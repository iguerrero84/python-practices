import os


def get_filename_without_extension(path):
    base_name = os.path.basename(path)
    filename_without_extension, _ = os.path.splitext(base_name)
    return filename_without_extension


# Example usage:
file_path = "/path/to/your/file/NBR_FILE_OUTPUT.txt"
result = get_filename_without_extension(file_path)
print(type(result))
