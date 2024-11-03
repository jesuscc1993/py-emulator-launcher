import os
import winreg

python_path = input('Enter the full path to your Python executable (e.g., C:\\Python\\Python312\\pythonw.exe):\n').strip()

if not os.path.isfile(python_path):
  print(f'The path "{python_path}" does not point to a valid executable.')
else:
  try:
    with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, 'emu', 0, winreg.KEY_ALL_ACCESS) as key:
      winreg.SetValueEx(key, 'URL Protocol', 0, winreg.REG_SZ, '')
      winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'URL: Emulator Protocol')

    with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r'emu\shell\open\command') as command_key:
      command_value = f'"{python_path}" "{os.getcwd()}\\emulator_launcher.py" "%1"'
      winreg.SetValueEx(command_key, '', 0, winreg.REG_SZ, command_value)

    print('Registry entries created successfully.')

  except Exception as e:
    print(f'An error occurred: {e}')

input('Press Enter to exit...')
