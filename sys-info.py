import os
import sys
import platform

print("=" * 40)
print("System Information Report")
print("=" * 40)

# 1. Print current username
username = os.getlogin()
print(f"Current Username: {username}")

# 2. Print current working directory
directory = os.getcwd()
print(f"Current Working Directory: {directory}")

# 3. Print OS name
os_name = platform.system()
print(f"Operating System: {os_name}")

# 4. Print OS version/release
os_version = platform.release()
print(f"OS Version: {os_version}")

# 5. Print machine architecture/processor type
architecture = platform.machine()
print(f"Machine Architecture: {architecture}")

# 6. Print Python version/ sys.version
python_version = sys.version
print(f"Python Version: {python_version}")


print("=" * 40)
print("Files in Current Directory")
print("=" * 40)

# 7. Get the list of files (hidden and shown) in the current directory and print them
files = os.listdir(directory)

# 8. Print each file in the list
for file in files:
    print(" -", file)

# 9. Print the total number of files in the current directory
total_files = len(files)
print(f"Total Number of Files: {total_files}")


print("=" * 40) 
print("End of System Information Report")
print("=" * 40)


while True:
    user_input = input("Press Enter to exit...")

    if user_input == "":
        break
    else:
        print("Invalid input. Please press Enter to exit.")
