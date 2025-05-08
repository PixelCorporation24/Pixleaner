import requests
import re
import subprocess

def get_installed_drivers():
    try:
        result = subprocess.run(["pnputitl", "/enum-drivers"],
            capture_output=True, text=True, check=True)
        drivers = re.findall(r"Published Name: (oem\d+\.inf)\s+Original Name: (.*?)\s+Provider Name: (.*?)\Driver Version: (\d+\.\d+\.\d+)", result.stdout)
        driver_list = [
            {
                "Published Name": d[0],
                "Original Name": d[1],
                "Provider Name": d[2],
                "Class Name": d[3],
                "Driver Version": d[4]
            }
            for d in drivers
            ]
        return driver_list
    except subprocess.CalledProcessError as e:
        print("Erro ao obter drivers instalados:", e)
        return[]
            
def check_for_updates(drivers):
    updates_available = []
    for drivers in drivers:
        latest_version = get_latest_driver_version(driver["Original Name"], driver ["Provider Name"])
        if latest_version and latest_version > driver["Driver Version"]:
            updates_available.append({
                "Driver": driver["Original Name"],
                "Installed Version": driver["Driver Version"],
                "Latest Version": latest_version
            })
    return updates_available
    
def notify_user(updates):
    if updates:
        print("Atualização de drivers disponível:")
        for update in updates:
            print(f"{update['Driver']}: {update['Installed Version']} -> {update['Latest Version']}")
        
