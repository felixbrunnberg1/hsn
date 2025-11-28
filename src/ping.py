import subprocess
import platform

def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "4", host]

    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    out, err = proc.communicate()
    output = out.lower() + err.lower()
    print(output)

    if "0 received" in output:
        return False
    else:
        return True
