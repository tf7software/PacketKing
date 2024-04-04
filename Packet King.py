import tkinter as tk
from tkinter import messagebox
import subprocess

def set_udp_packet_size():
    """Attempts to set the UDP packet size to 65536 bytes by editing sysctl.conf with administrative privileges.

    Displays a success message box if successful, otherwise displays an error message box
    providing guidance to the user.
    """

    try:
        # Execute AppleScript to write to sysctl.conf with elevated privileges
        applescript = """
        do shell script "echo '\nnet.inet.udp.maxdgram=65536' >> /etc/sysctl.conf" with administrator privileges
        """
        subprocess.run(['osascript', '-e', applescript], check=True)

        # Show success message
        messagebox.showinfo("Success", "UDP packet size set to 65536 bytes. Please restart your system for changes to take effect.")

        # Add a "Restart Now" button
        restart_button = tk.Button(root, text="Restart Now", command=restart_system)
        restart_button.pack(pady=10)

    except subprocess.CalledProcessError as e:
        error_message = f"Failed to set UDP packet size: {e}"
        messagebox.showerror("Error", error_message)
    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        messagebox.showerror("Error", error_message)

def restart_system():
    """Restarts the system."""
    subprocess.run(['osascript', '-e', 'tell app "System Events" to restart'])

# Create the main window with a more descriptive title
root = tk.Tk()
root.title("TF7Network Pro - UDP Packet Size Adjuster")
root.resizable(False, False)  # Set window to be unresizable

# Create and pack the warning label with a clearer message
warning_label = tk.Label(root, text="Warning: Use with caution! Incorrect settings may disrupt network functionality.", fg="red")
warning_label.pack(pady=10)

# Create and pack the button with a more informative label
start_button = tk.Button(root, text="Set UDP Packet Size (Requires Admin Privileges)", command=set_udp_packet_size)
start_button.pack(pady=10)

# Create and pack the label at the bottom
bottom_label = tk.Label(root, text="© TwentyFour7 Software 2024")
bottom_label.pack(pady=10)

# Run the GUI
root.mainloop()
