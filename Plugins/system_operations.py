import os
import math
import psutil
import time
from random import randint
import subprocess
import AppOpener
from pynput.keyboard import Key, Controller
from PIL import ImageGrab
import wmi
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class SystemTasks:
    def __init__(self):
        self.keyboard = Controller()

    def write(self, text):
        self.keyboard.type(text)

    def select(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('a')
        self.keyboard.release('a')
        self.keyboard.release(Key.ctrl)

    def hitEnter(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

    def delete(self):
        self.select()
        self.keyboard.press(Key.backspace)
        self.keyboard.release(Key.backspace)

    def copy(self):
        self.select()
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('c')
        self.keyboard.release('c')
        self.keyboard.release(Key.ctrl)

    def paste(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('v')
        self.keyboard.release('v')
        self.keyboard.release(Key.ctrl)

    def new_file(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('n')
        self.keyboard.release('n')
        self.keyboard.release(Key.ctrl)

    def save(self, name):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('s')
        self.keyboard.release('s')
        self.keyboard.release(Key.ctrl)
        time.sleep(0.2)
        self.write(name)
        self.hitEnter()


class TabOpt:
    def __init__(self):
        self.keyboard = Controller()

    def switchTab(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.tab)
        self.keyboard.release(Key.tab)
        self.keyboard.release(Key.ctrl)

    def closeTab(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('w')
        self.keyboard.release('w')
        self.keyboard.release(Key.ctrl)

    def newTab(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('t')
        self.keyboard.release('t')
        self.keyboard.release(Key.ctrl)


class WindowOpt:
    def __init__(self):
        self.keyboard = Controller()

    def closeWindow(self):
        self.keyboard.press(Key.alt_l)
        self.keyboard.press(Key.f4)
        self.keyboard.release(Key.f4)
        self.keyboard.release(Key.alt_l)

    def minimizeWindow(self):
        for i in range(2):
            self.keyboard.press(Key.cmd)
            self.keyboard.press(Key.down)
            self.keyboard.release(Key.down)
            self.keyboard.release(Key.cmd)
            time.sleep(0.05)

    def maximizeWindow(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.up)
        self.keyboard.release(Key.up)
        self.keyboard.release(Key.cmd)

    def switchWindow(self):
        self.keyboard.press(Key.alt_l)
        self.keyboard.press(Key.tab)
        self.keyboard.release(Key.tab)
        self.keyboard.release(Key.alt_l)

    def Screen_Shot(self):
        im = ImageGrab.grab()
        im.save(f'C:/Users/LEGION/Desktop/screenshots/picture_{randint(1, 100)}.jpg')
        return True

def systemInfo():
    c = wmi.WMI()
    my_system_1 = c.Win32_LogicalDisk()[0]
    my_system_2 = c.Win32_ComputerSystem()[0]
    info = f"Total Disk Space: {round(int(my_system_1.Size)/(1024**3),2)} GB\n" \
           f"Free Disk Space: {round(int(my_system_1.Freespace)/(1024**3),2)} GB\n" \
           f"Manufacturer: {my_system_2.Manufacturer}\n" \
           f"Model: {my_system_2. Model}\n" \
           f"Owner: {my_system_2.PrimaryOwnerName}\n" \
           f"Number of Processors: {psutil.cpu_count()}\n" \
           f"System Type: {my_system_2.SystemType}"
    return info


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def system_stats():
    cpu_stats = str(psutil.cpu_percent())
    battery_percent = psutil.sensors_battery().percent
    memory_in_use = convert_size(psutil.virtual_memory().used)
    total_memory = convert_size(psutil.virtual_memory().total)
    stats = f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory} is being used and " \
                f"battery level is at {battery_percent}%"
    return stats


def app_path(app):
    app_paths = {'access': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\ACCICONS.exe',
                 'powerpoint': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\POWERPNT.exe',
                 'word': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\WINWORD.exe',
                 'excel': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\EXCEL.exe',
                 'outlook': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\OUTLOOK.exe',
                 'onenote': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\ONENOTE.exe',
                 'publisher': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\MSPUB.exe',
                 'sharepoint': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\GROOVE.exe',
                 'infopath designer': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\INFOPATH.exe',
                 'infopath filler': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\INFOPATH.exe',
                 'notepad' : 'C:\\Windows\\System32\\notepad.exe'}
    try:
        return app_paths[app]
    except KeyError:
        return None


def open_app(query):
    ms_office = ('access', 'powerpoint', 'word', 'excel', 'outlook', 'onenote', 'publisher', 'sharepoint', 'infopath designer',
                 'infopath filler','notepad')
    for app in ms_office:
        if app in query:
            path = app_path(app)
            subprocess.Popen(path)
            return True
    AppOpener.run(query[5:])
    return True

def take_note(note):
    time.sleep(0.2)
    sys_task = SystemTasks()
    sys_task.write(note)
    file_name = f"note_{randint(1, 100)}.txt"
    with open(file_name, "w") as file:
        file.write(note)
    # Open the file in Notepad
    os.system(f"notepad {file_name}")
    return True

def system_brightness(query):
    query=query.split()
    w = wmi.WMI(namespace='wmi')
    for item in w.WmiMonitorBrightness():
        volume = item.CurrentBrightness
    if "set" in query:
        for i in query:
            if "%" in i:
                volume=int(i[:len(i)-1])
        
        brightness_methods = w.WmiMonitorBrightnessMethods()[0]
        brightness_methods.WmiSetBrightness(volume, 0)

    elif "increase" in query:
        if volume<80:
            brightness_methods = w.WmiMonitorBrightnessMethods()[0]
            brightness_methods.WmiSetBrightness(volume+20, 0)
        else:
            brightness_methods = w.WmiMonitorBrightnessMethods()[0]
            brightness_methods.WmiSetBrightness(100, 0)
    elif "decrease" in query:
        if volume<20:
            brightness_methods = w.WmiMonitorBrightnessMethods()[0]
            brightness_methods.WmiSetBrightness(0, 0)
        else:
            brightness_methods = w.WmiMonitorBrightnessMethods()[0]
            brightness_methods.WmiSetBrightness(volume-20, 0)
    for item in w.WmiMonitorBrightness():
        volume = item.CurrentBrightness
       
    return f"Your brightness is set to {volume} percent"

def system_volume(query):
    query=query.split()

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get the current volume level (0.0 to 1.0)
    current_volume = volume.GetMasterVolumeLevelScalar()

    if "set" in query:
        for i in query:
            if "%" in i:
                vol_per=int(i[:len(i)-1])

                volume.SetMasterVolumeLevelScalar(vol_per/100, None)

    elif "increase" in query:
        if current_volume<0.8:
            volume.SetMasterVolumeLevelScalar(current_volume+0.2, None)
        else:
            volume.SetMasterVolumeLevelScalar(1.0, None)

    elif "decrease" in query:
        if current_volume>0.2:
            volume.SetMasterVolumeLevelScalar(current_volume-0.2, None)
        else:
            volume.SetMasterVolumeLevelScalar(0.0, None)

    current_volume = round(volume.GetMasterVolumeLevelScalar()*100,2)
    return f"Your volume is set to { current_volume } percent"
    