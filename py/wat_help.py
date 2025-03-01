# help.py - List all basic CMD commands available in Windows

def show_help():
    print("CMD Help - List of all standard CMD commands\n")
    print("Available commands:\n")
    
    # List of basic CMD commands
    commands = {
        "dir": "Displays a list of files and subdirectories in a directory.",
        "cd": "Changes the current directory.",
        "echo": "Displays messages, or turns command echoing on or off.",
        "cls": "Clears the screen.",
        "del": "Deletes one or more files.",
        "copy": "Copies files from one location to another.",
        "move": "Moves one or more files from one location to another.",
        "rename": "Renames a file or directory.",
        "mkdir": "Creates a new directory.",
        "rmdir": "Removes an empty directory.",
        "type": "Displays the contents of a file.",
        "exit": "Exits the command prompt or batch script.",
        "cls": "Clears the command line screen.",
        "pause": "Pauses the execution of a batch file and displays the message 'Press any key to continue...'.",
        "exit": "Exits the command prompt.",
        "start": "Starts a program, command, or batch file.",
        "tasklist": "Displays a list of currently running processes.",
        "taskkill": "Ends one or more tasks or processes.",
        "ipconfig": "Displays IP configuration information for all network adapters.",
        "ping": "Sends a test message to another computer or network device.",
        "netstat": "Displays current network connections and listening ports.",
        "hostname": "Displays the name of the computer.",
        "shutdown": "Shuts down or restarts the computer.",
        "systeminfo": "Displays detailed configuration information about the computer and its operating system.",
        "set": "Displays or sets environment variables.",
        "cls": "Clears the console screen.",
        "assoc": "Displays or modifies file extension associations.",
        "chkdsk": "Checks the disk for errors and repairs them.",
        "format": "Formats a disk for use with Windows.",
        "sfc": "Scans and repairs system files.",
        "diskpart": "Manages disk partitions.",
        "bcdedit": "Displays or modifies boot configuration data.",
        "regedit": "Opens the registry editor to modify the Windows registry.",
        "fc": "Compares two files and displays the differences.",
        "find": "Searches for a text string in a file or files.",
        "findstr": "Searches for a string in files using regular expressions.",
        "robocopy": "Copies files and directories with more options than copy.",
        "xcopy": "Copies files and directories, including subdirectories.",
        "cipher": "Displays or alters the encryption of files and directories.",
        "net": "Manages network resources, such as shared folders or printers.",
        "net use": "Connects, disconnects, and displays network resources.",
        "net share": "Displays or modifies shared resources.",
        "net user": "Adds, deletes, or modifies user accounts on the computer.",
        "netstat": "Displays active network connections and statistics.",
        "path": "Displays or sets a command search path.",
        "setx": "Sets an environment variable permanently.",
        "ver": "Displays the version of the operating system.",
        "time": "Displays or sets the system time.",
        "date": "Displays or sets the system date.",
        "assoc": "Displays or modifies file extension associations.",
        "chdir": "Changes the current directory.",
        "cls": "Clears the command prompt screen.",
        "exit": "Exits the command prompt or batch file.",
        "tasklist": "Displays all currently running tasks.",
        "taskkill": "Ends tasks or processes based on their name or PID.",
        "mkdir": "Creates a new directory.",
        "rmdir": "Removes a directory.",
        "tree": "Graphically displays the directory structure of a drive or path.",
        "verify": "Verifies that files are written correctly to disk.",
        "xcopy": "Copies files and directories from one location to another."
    }

    # Display each command with a description
    for command, description in commands.items():
        print(f"{command}: {description}")

    print("\nFor more details on each command, refer to the official Microsoft documentation.")
    print("https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/")

# Calling the show_help function when this script is run
if __name__ == "__main__":
    show_help()
