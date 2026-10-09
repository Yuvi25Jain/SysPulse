import psutil
import platform
import socket

def get_metrics():
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent
    }