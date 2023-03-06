import subprocess

# Prompt the user to select a file to send
file_path = input("Enter the path of the file you want to send: ")

# Use AppleScript to automate the file transfer via Bluetooth
script = """
tell application "Finder"
	set theFile to POSIX file "{file_path}" as alias
end tell

tell application "System Events"
	tell process "Finder"
		set frontmost to true
		keystroke "b" using {command down, shift down}
		delay 1
		keystroke return
		delay 1
		keystroke tab
		delay 1
		keystroke tab
		delay 1
		keystroke tab
		delay 1
		keystroke return
		delay 1
		keystroke "{file_path}"
		delay 1
		key code 48
	end tell
end tell
""".format(file_path=file_path)

# Execute the AppleScript using the osascript command
subprocess.call(['osascript', '-e', script])
