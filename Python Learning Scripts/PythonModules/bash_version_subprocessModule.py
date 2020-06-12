#to get only the java version installed on the OS.

import subprocess
cmd='bash --version'
JAVA_VERSION_COMMAND=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
JAVA_COMMAND_RC=JAVA_VERSION_COMMAND.wait()
OUTPUT,ERROR=JAVA_VERSION_COMMAND.communicate()
if JAVA_COMMAND_RC == 0:
    for EACH in OUTPUT.splitlines():
        if "version" in EACH and "release" in EACH:
            print(f"Bash Version: {EACH.split()[3].split('(')[0]}")
else:    
    print(f"{ERROR}")

