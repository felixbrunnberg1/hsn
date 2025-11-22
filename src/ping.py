import subprocess
import platform

def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]

    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    out, err = proc.communicate()
    output = out.lower() + err.lower()
    
    if "ttl=" in output:
        return True
    else:
        return False
    