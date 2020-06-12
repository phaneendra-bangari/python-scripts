#to find the java version on any OS.
import subprocess
cmd="java -version"
JAVA_COMMAND=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
JAVA_COMMAND_RC=JAVA_COMMAND.wait()
JAVA_OUTPUT,JAVA_ERROR=JAVA_COMMAND.communicate()
if JAVA_COMMAND_RC == 0:
    if bool(JAVA_OUTPUT) == True:
        print(JAVA_OUTPUT)

    if bool(JAVA_OUTPUT) == False and bool(JAVA_ERROR) == True:
        print(JAVA_ERROR.splitlines()[0].split()[2].strip("\""))
else:
    print(JAVA_ERROR)
