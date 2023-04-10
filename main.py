import subprocess

# Membuat input untuk cmd

expired = "0"

def vmess(user):
    cmd_input = f"{user}\n{expired}\n"

# Menjalankan cmd dengan input
    process = subprocess.Popen(['/usr/bin/add-vmess'], stdin=subprocess.PIPE)
    out = process.communicate(input=cmd_input.encode())
    return out


def vless(user):
    cmd_input = f"{user}\n{expired}\n"

# Menjalankan cmd dengan input
    process = subprocess.Popen(['/usr/bin/add-vmess'], stdin=subprocess.PIPE)
    process.communicate(input=cmd_input.encode())

if __name__ == "__main__":
    print(vmess("fsdhua") )
