import base64
import os
import subprocess
import sys

emulators = {
  'bsnes': (f'/bSNES/bsnes_hd.exe', ''),
  'cemu': (f'/Cemu/Cemu.exe', '-f -g'),
  'citra': (f'/Citra/citra-qt.exe', ''),
  'desmume': (f'/DeSmuME/DeSmuME.exe', ''),
  'dolphin': (f'/Dolphin/Dolphin.exe', ''),
  'duckstation': (f'/DuckStation/duckstation-qt-x64-ReleaseLTCG.exe', ''),
  'mgba': (f'/mGBA/mGBA.exe', ''),
  'p64': (f'/Project64/Project64.exe', ''),
  'pcsx2': (f'/PCSX2/pcsx2-qt.exe', ''),
  'ppsspp': (f'/PPSSPP/PPSSPPWindows64.exe', ''),
  'rpcs3': (f'/RPCS3/rpcs3.exe', ''),
  'ryujinx': (f'/Ryujinx/Ryujinx.exe', ''),
  'vba': (f'/VisualBoyAdvance-M/visualboyadvance-m.exe', ''),
  'vita3k': (f'/Vita3K/Vita3K.exe', ''),
  'xemu': (f'/Xemu/xemu.exe', '-full-screen -dvd_path'),
  'xenia': (f'/Xenia/xenia_canary.exe', ''),
  'yuzu': (f'/yuzu/yuzu-early-access/yuzu.exe', ''),
}

def main():
  if len(sys.argv) < 2:
    print('No URL provided.')
    input('Press Enter to exit...')
    return

  encoded_params = sys.argv[1].replace('emu://', '').rstrip('/')
  params = base64.b64decode(encoded_params).decode('utf-8')
  emulators_home, emulator, rom = params.split(';')
  rom = rom.replace('/', '\\')

  # print(f'DEBUG:\n rootPath: {emulators_home}\n emulator: {emulator}\n rom: {rom}')

  if emulator in emulators:
    emulator, arguments = emulators[emulator]
    emulator = f'{emulators_home}/{emulator}'
    arguments = arguments.split() if arguments else []

    if os.path.exists(emulator):
      command = [emulator] + arguments + [rom]
      # print(f'DEBUG:\n command: {command}')
      subprocess.run(command)
    else:
      print(f'Executable not found: {emulator}')
      input('Press Enter to exit...')
  else:
    print(f'Emulator not found: {emulator}')
    input('Press Enter to exit...')

if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    print(f'An unexpected error occurred: {e}')
    input('Press Enter to exit...')
