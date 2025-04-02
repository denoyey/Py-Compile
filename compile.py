import marshal, base64, zlib, sys, os, readline, time, subprocess, termcolor, datetime, string, random, shutil
from termcolor import colored
from setuptools import setup
from Cython.Build import cythonize

def clear_screen():
    subprocess.run(['cls' if os.name == 'nt' else 'clear'])
    time.sleep(1)
    
def copyright():
    tahun = datetime.datetime.now().year
    copyright_text = colored(f"Github: github.com/denoyey || © {tahun} All Rights Reserved.", 'light_grey', attrs=['reverse'])
    return(copyright_text)

def logo():
    print(colored(f"""

██▄   ▄███▄      ▄   ████▄ ▀▄    ▄ ▄███▄ ▀▄    ▄ 
█  █  █▀   ▀      █  █   █   █  █  █▀   ▀  █  █  
█   █ ██▄▄    ██   █ █   █    ▀█   ██▄▄     ▀█   
█  █  █▄   ▄▀ █ █  █ ▀████    █    █▄   ▄▀  █    
███▀  ▀███▀   █  █ █        ▄▀     ▀███▀  ▄▀     
              █   ██                                                                            
{copyright()}
    """, 'light_grey', attrs=['bold']))
    
INSTALLATION_FILE = "installation_done.txt"

def instalation():
    def is_installed(command):
        result = subprocess.run(['which', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    if os.path.exists(INSTALLATION_FILE):
        return
    clear_screen()
    print(colored("\nMengecek apakah Python3 dan pip sudah terinstal...", 'light_grey', attrs=['reverse']))
    if is_installed('python3'):
        print(colored("\nPython3 sudah terinstal.", 'light_green', attrs=['bold']))
    else:
        print(colored("\nPython3 belum terinstal, menginstal python3...", 'light_red', attrs=['bold']))
        subprocess.run(['sudo', 'apt', 'install', 'python3', '-y'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if is_installed('pip3'):
        print(colored("\nPip sudah terinstal.", 'light_green', attrs=['bold']))
    else:
        print(colored("\npip belum terinstal, menginstal pip...", 'light_red', attrs=['bold']))
        subprocess.run(['sudo', 'apt', 'install', 'python3-pip', '-y'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if is_installed('subdora'):
        print(colored("\nSubdora sudah terinstal.", 'light_green', attrs=['bold']))
    else:
        print(colored("\nSubdora belum terinstal, menginstal Subdora...", 'light_red', attrs=['bold']))
        subprocess.run(['pip', 'install', 'subdora', '--break-system-packages'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with open(INSTALLATION_FILE, 'w') as f:
        f.write("Installation complete.")
    time.sleep(2)
    clear_screen()

def obfuscate_python_marshal(input_file, output_file):
    clear_screen()
    logo()
    print(colored('\n[ === 🔒 ENCODE MARSHAL 🔒 === ]', 'light_yellow', attrs=['bold']))
    with open(input_file, 'r') as file:
        source_code = file.read()
    bytecode = compile(source_code, input_file, 'exec')
    marshaled_code = marshal.dumps(bytecode)
    with open(output_file, 'w') as out_file:
        out_file.write("# Obfus-code by denoyey\n")
        out_file.write("# github.com/denoyey\n\n\n")
        out_file.write("import marshal\n")
        out_file.write("code = ")
        out_file.write(f"({repr(marshaled_code)})")
        out_file.write("\n")
        out_file.write("exec(marshal.loads(code))\n")
    print(colored(f"\nFile Python terencode dan disimpan sebagai: {output_file}\n", 'light_green', attrs=['reverse']))
    time.sleep(1.5)
    again()

def obfuscate_python_base64(input_file, output_file):
    clear_screen()
    logo()
    print(colored('\n[ === 🔒 ENCODE BASE64 🔒 === ]', 'light_green', attrs=['bold']))
    with open(input_file, 'r') as file:
        source_code = file.read()
    encoded_code = base64.b64encode(source_code.encode('utf-8')).decode('utf-8')
    with open(output_file, 'w') as out_file:
        out_file.write("# Obfus-code by denoyey\n")
        out_file.write("# github.com/denoyey\n\n\n")
        out_file.write("import base64\n")
        out_file.write("encoded_code = ")
        out_file.write(f"('{encoded_code}')\n")
        out_file.write("decoded_code = base64.b64decode(encoded_code).decode('utf-8')\n")
        out_file.write("exec(decoded_code)\n")
    print(colored(f"\nFile Python terencode dan disimpan sebagai: {output_file}\n", 'light_green', attrs=['reverse']))
    time.sleep(1.5)
    again()

def obfuscate_python_zlib(input_file, output_file):
    clear_screen()
    logo()
    print(colored('\n[ === 🔒 ENCODE ZLIB 🔒 === ]', 'light_magenta', attrs=['bold']))
    with open(input_file, 'r') as file:
        code = file.read()
    compressed_code = zlib.compress(code.encode('utf-8'))
    with open(output_file, 'w') as out_file:
        out_file.write("# Obfus-code by denoyey\n")
        out_file.write("# github.com/denoyey\n\n\n")
        out_file.write("import zlib\n")
        out_file.write("compressed_code = ")
        out_file.write(f"({repr(compressed_code)})\n")
        out_file.write("code = zlib.decompress(compressed_code).decode('utf-8')\n")
        out_file.write("exec(code)\n")
    print(colored(f"\n\nFile Python terencode dan disimpan sebagai: {output_file}\n", 'light_green', attrs=['reverse']))
    time.sleep(1.5)
    again()

def obfuscate_python_marshal_base64(input_file, output_file):
    clear_screen()
    logo()
    print(colored('\n[ === 🔒 ENCODE MARSHAL+BASE64 🔒 === ]', 'light_cyan', attrs=['bold']))
    with open(input_file, 'r') as file:
        source_code = file.read()
    bytecode = compile(source_code, input_file, 'exec')
    marshaled_code = marshal.dumps(bytecode)
    encoded_code = base64.b64encode(marshaled_code).decode('utf-8')
    with open(output_file, 'w') as out_file:
        out_file.write("# Obfus-code by denoyey\n")
        out_file.write("# github.com/denoyey\n\n\n")
        out_file.write("import base64, marshal\n")
        out_file.write("encoded_code = ")
        out_file.write(f"('{encoded_code}')\n")
        out_file.write("decoded_code = base64.b64decode(encoded_code)\n")
        out_file.write("exec(marshal.loads(decoded_code))\n")
    print(colored(f"\n\nFile Python terencode dan disimpan sebagai: {output_file}\n", 'light_green', attrs=['reverse']))
    time.sleep(1.5)
    again()

def obfuscate_python_marshal_zlib_base64(input_file, output_file):
    clear_screen()
    logo()
    print(colored('\n[ === 🔒 ENCODE MARSHAL+ZLIB+BASE64 🔒 === ]', 'light_blue', attrs=['bold']))
    with open(input_file, 'r') as file:
        source_code = file.read()
    bytecode = compile(source_code, input_file, 'exec')
    marshaled_code = marshal.dumps(bytecode)
    compressed_code = zlib.compress(marshaled_code)
    encoded_code = base64.b64encode(compressed_code).decode('utf-8')
    with open(output_file, 'w') as out_file:
        out_file.write("# Obfus-code by denoyey\n")
        out_file.write("# github.com/denoyey\n\n\n")
        out_file.write("import base64, zlib, marshal\n")
        out_file.write("encoded_code = ")
        out_file.write(f"('{encoded_code}')\n")
        out_file.write("decoded_code = base64.b64decode(encoded_code)\n")
        out_file.write("decompressed_code = zlib.decompress(decoded_code)\n")
        out_file.write("exec(marshal.loads(decompressed_code))\n")
    print(colored(f"\n\nFile Python terencode dan disimpan sebagai: {output_file}\n", 'light_green', attrs=['reverse']))
    time.sleep(1.5)
    again()
    
def obfuscate_python_simpleobfus(input_file, output_file, key):
    clear_screen()
    logo()
    print(colored('\n[ === 🔒 ENCODE SIMPLEOBFUS 🔒 === ]', 'light_magenta', attrs=['bold']))
    try:
        with open(input_file, 'r') as file:
            python_code = file.read()
        if not python_code:
            print("File input kosong.")
            return
        obfuscated_program = "".join(chr(ord(c) ^ key) for c in python_code)
        encoded = base64.b64encode(obfuscated_program.encode()).decode()
        obfuscated_code = """# Obfus-code by denoyey
# github.com/denoyey

import base64
def decode_and_execute():
    encoded = "{}"
    decoded = base64.b64decode(encoded)
    decoded_code = "".join(chr(ord(c) ^ {}) for c in decoded.decode())
    exec(decoded_code)
decode_and_execute()
""".format(encoded, key)
        with open(output_file, 'w') as file:
            file.write(obfuscated_code)
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(2)
    print(colored(f'\nScript {input_file} telah selesai diencode.', 'light_green', attrs=['reverse']))
    again()

def obfuscate_python_pyfuscator(input_file, output_file, key):
    clear_screen()
    logo()
    print(colored('\n[ === 🔒 ENCODE PYFUSCATOR 🔒 === ]', 'light_green', attrs=['bold']))
    with open(input_file, 'r') as file:
        python_code = file.read()
    obfuscated_program = "".join(chr(ord(c) ^ key) for c in python_code)
    encoded = base64.b64encode(obfuscated_program.encode()).decode()
    obfuscated_code = '__GITHUB__DENOYEY___GITHUB__DENOYEY__ = ""\n'
    for i in range(0, len(encoded), 10):
        chunk = encoded[i:i+10]
        hex_chunk = ''.join(['\\x{:02x}'.format(ord(c)) for c in chunk])
        obfuscated_code += '__GITHUB__DENOYEY___GITHUB__DENOYEY__ += "{}"\n'.format(hex_chunk)
    obfuscated_code += 'exec("".join(chr(ord(c) ^ {}) for c in __import__("base64").b64decode(__GITHUB__DENOYEY___GITHUB__DENOYEY__).decode()))'.format(key)
    with open(output_file, 'w') as file:
        file.write(obfuscated_code)

def obfuscate_python_cython(input_file, output_folder="output_cython"):
    clear_screen()
    logo()
    print(colored('\n[ === 🔒 ENCODE CYTHON 🔒 === ]\n', 'light_red', attrs=['bold']))
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if not os.path.isfile(input_file):
        print(f"Error: File {input_file} tidak ditemukan.")
        return
    def setup_cython():
        setup(
            ext_modules=cythonize(
                input_file,
                compiler_directives={"language_level": "3"}
            ),
            script_args=["build_ext", "--inplace"],
            options={'build_ext': {'build_lib': output_folder}}
        )
    print(f"\nMengkompilasi {input_file} menjadi Cython...")
    setup_cython()
    module_name = os.path.splitext(os.path.basename(input_file))[0]
    cython_file_path = os.path.join(output_folder, f"{module_name}.so")
    python_file_path = os.path.join(output_folder, f"{module_name}.py")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.exists(cython_file_path):
        target_file = cython_file_path
    elif os.path.exists(python_file_path):
        target_file = python_file_path
    elif os.path.exists(os.path.join(current_dir, f"{module_name}.py")):
        target_file = os.path.join(current_dir, f"{module_name}.py")
    else:
        print(f"Error: File {module_name}.py atau {module_name}.so tidak ditemukan di {output_folder} atau di direktori yang sama.")
        return
    with open(os.path.join(output_folder, "run.py"), 'w') as f:
        f.write(f"""# Obfus-code by denoyey
# github.com/denoyey


import os, sys
try:
    __import__("{module_name}") # Bisa menambahkan .main() --> isi sesuai fungsi yg mau dipanggil
except Exception as e:
    exit(str(e))
""")
    time.sleep(1)
    clear_screen()
    print(colored(f'\nScript {input_file} telah selesai diencode.', 'light_green', attrs=['reverse']))
    print(colored(f'\nUntuk menjalankan, ketik: (python run.py)', 'light_yellow', attrs=['bold']))
    print(colored(f'Atau jika file run ada di dalam folder, ketik: (python output_cython/run.py)', 'light_yellow', attrs=['bold']))
    time.sleep(1.5)
    again()

def again():
    while True:
        againInput = input(colored("\nApakah ingin compile lagi (y/n): ", 'light_grey', attrs=['bold']))
        if againInput.lower() == 'y':
            clear_screen()
            main()
            break
        elif againInput.lower() == 'n':
            clear_screen()
            logo()
            print(colored("\nTerimakasih sudah menggunakan program ini.", 'light_yellow', attrs=['bold']))
            subprocess.run(['sudo', 'apt', 'autoremove', '-y'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            exit()
        else:
            clear_screen()
            print(colored("\nPilihan anda tidak valid.", 'light_red', attrs=['bold']))

def setup_tab_completion():
    def complete_file_path(text, state):
        files = [f for f in os.listdir() if f.startswith(text) and f.endswith(".py")]
        try:
            return files[state]
        except IndexError:
            return None
    readline.set_completer(complete_file_path)
    readline.parse_and_bind("tab: complete")

def show_menu():
    clear_screen()
    logo()
    print(colored("\n[ === TOOLS FOR ENCRYPTOR === ]\n", 'light_grey', attrs=['bold']))
    print(colored("[1] Encode Marshal", 'light_yellow', attrs=['bold']))
    print(colored("[2] Encode Base64", 'light_green', attrs=['bold']))
    print(colored("[3] Encode Zlib", 'light_magenta', attrs=['bold']))
    print(colored("[4] Encode Marshal+Base64", 'light_cyan', attrs=['bold']))
    print(colored("[5] Encode Marshal+Zlib+Base64", 'light_blue', attrs=['bold']))
    print(colored("[6] Encode Simpleobfus", 'light_magenta', attrs=['bold']))
    print(colored("[7] Encode Pyfuscator", 'light_green', attrs=['bold']))
    print(colored("[8] Encode Cython", 'light_red', attrs=['bold']))
    print(colored("[0] Exit", 'light_grey', attrs=['bold']))
    pilihan = input(colored("\n[?] Silahkan pilih menu: ", 'light_grey', attrs=['bold']))
    return pilihan

def main():
    instalation()
    setup_tab_completion()
    while True:
        pilihan = show_menu()
        if pilihan == '1':
            clear_screen()
            logo()
            input_file = input(colored("\nMasukkan file Python (e.g example.py/directory): ", 'light_grey', attrs=['bold']))
            if os.path.exists(input_file) and input_file.endswith(".py"):
                output_file = input(colored("\nMasukkan nama file output (e.g shal.py): ", 'light_grey', attrs=['bold']))
                obfuscate_python_marshal(input_file, output_file)
            else:
                print(colored("\nFile tidak ditemukan atau bukan file Python (.py).", 'light_red', attrs=['reverse']))
        elif pilihan == '2':
            clear_screen()
            logo()
            input_file = input(colored("\nMasukkan file Python (e.g example.py/directory): ", 'light_grey', attrs=['bold']))
            if os.path.exists(input_file) and input_file.endswith(".py"):
                output_file = input(colored("\nMasukkan nama file output (e.g bs64.py): ", 'light_grey', attrs=['bold']))
                obfuscate_python_base64(input_file, output_file)
            else:
                print(colored("\nFile tidak ditemukan atau bukan file Python (.py).", 'light_red', attrs=['reverse']))
        elif pilihan == '3':
            clear_screen()
            logo()
            input_file = input(colored("\nMasukkan file Python (e.g example.py/directory): ", 'light_grey', attrs=['bold']))
            if os.path.exists(input_file) and input_file.endswith(".py"):
                output_file = input(colored("\nMasukkan nama file output (e.g zzlib.py): ", 'light_grey', attrs=['bold']))
                obfuscate_python_zlib(input_file, output_file)
            else:
                print(colored("\nFile tidak ditemukan atau bukan file Python (.py).", 'light_red', attrs=['reverse']))
        elif pilihan == '4':
            clear_screen()
            logo()
            input_file = input(colored("\nMasukkan file Python (e.g example.py/directory): ", 'light_grey', attrs=['bold']))
            if os.path.exists(input_file) and input_file.endswith(".py"):
                output_file = input(colored("\nMasukkan nama file output (e.g shalbs64.py): ", 'light_grey', attrs=['bold']))
                obfuscate_python_marshal_base64(input_file, output_file)
            else:
                print(colored("\nFile tidak ditemukan atau bukan file Python (.py).", 'light_red', attrs=['reverse']))
        elif pilihan == '5':
            clear_screen()
            logo()
            input_file = input(colored("\nMasukkan file Python (e.g example.py/directory): ", 'light_grey', attrs=['bold']))
            if os.path.exists(input_file) and input_file.endswith(".py"):
                output_file = input(colored("\nMasukkan nama file output (e.g shalzzlibbs64.py): ", 'light_grey', attrs=['bold']))
                obfuscate_python_marshal_zlib_base64(input_file, output_file)
            else:
                print(colored("\nFile tidak ditemukan atau bukan file Python (.py).", 'light_red', attrs=['reverse']))
        elif pilihan == '6':
            clear_screen()
            logo()
            input_file = input(colored("\nMasukkan file Python (e.g example.py/directory): ", 'light_grey', attrs=['bold']))
            if os.path.exists(input_file) and input_file.endswith(".py"):
                output_file = input(colored("\nMasukkan nama file output (e.g simpleobfus.py): ", 'light_grey', attrs=['bold']))
                key = 0x7F
                obfuscate_python_simpleobfus(input_file, output_file, key)
            else:
                print(colored("\nFile tidak ditemukan atau bukan file Python (.py).", 'light_red', attrs=['reverse']))
        elif pilihan == '7':
            clear_screen()
            logo()
            input_file = input(colored("\nMasukkan file Python (e.g example.py/directory): ", 'light_grey', attrs=['bold']))
            if os.path.exists(input_file) and input_file.endswith(".py"):
                output_file = input(colored("\nMasukkan nama file output (e.g pyfuscat0r.py): ", 'light_grey', attrs=['bold']))
                key = 0x7F
                obfuscate_python_pyfuscator(input_file, output_file, key)
            else:
                print(colored("\nFile tidak ditemukan atau bukan file Python (.py).", 'light_red', attrs=['reverse']))
        elif pilihan == '8':
            clear_screen()
            logo()
            input_file = input(colored("\nMasukkan file Python (e.g example.py/directory): ", 'light_grey', attrs=['bold']))
            if os.path.exists(input_file) and input_file.endswith(".py"):
                obfuscate_python_cython(input_file)
            else:
                print(colored("\nFile tidak ditemukan atau bukan file Python (.py).", 'light_red', attrs=['reverse']))
        elif pilihan == '0':
            clear_screen()
            logo()
            print(colored("\nTerimakasih sudah menggunakan program ini.", 'light_yellow', attrs=['bold']))
            exit()
        else:
            clear_screen()
            logo()
            print(colored("\nPilihan anda tidak valid, silahkan coba lagi.", 'light_red', attrs=['bold']))

# Jalankan Pogram.
main()
