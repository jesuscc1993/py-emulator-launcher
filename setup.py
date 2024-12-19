import os
import winreg

python_path = rf"{os.environ['PYTHONHOME'].split(os.pathsep)[0]}\pythonw.exe"
print(f'Found Python path: "{python_path}"')

try:
  with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r'emu') as key:
    winreg.SetValueEx(key, 'URL Protocol', 0, winreg.REG_SZ, '')
    winreg.SetValueEx(key, '', 0, winreg.REG_SZ, 'URL: Emulator Protocol')

  with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r'emu\shell\open\command') as command_key:
    command_value = f'"{python_path}" "{os.getcwd()}\\emulator_launcher.py" "%1"'
    winreg.SetValueEx(command_key, '', 0, winreg.REG_SZ, command_value)

  print('Registry entries created successfully.')

except Exception as e:
  print(f'An error occurred: {e}')

input('Press Enter to exit...')
