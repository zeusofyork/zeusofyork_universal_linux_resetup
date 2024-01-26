import lzma
import os
import subprocess


menu = input("""Please select from the following options: 
    1. Linux
    2. Windows
    3. Android""" + '\n')





def send_command(linux_apps,command):
 
    sent_command = str(command)
    result1 = subprocess.run(sent_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Get the output and error (if any)
    output1 = result1.stdout
    error1 = result1.stderr
            # Check if the command was successful
    if result1.returncode == 0:
        print("Command executed successfully!")
        print("Output:\n", output1)
    else:
        print("Command failed with return code:", result1.returncode)
        if error1:
            print("Error:\n", error1)
        else:
            print('test')




if int(menu) == 1:
    linux_tools = input("""Which tools? 
        1. Linux re-installation tools
        2. Kernel Builder
        """)
    if int(linux_tools) == 1:
        linux_tools_submenu = input("""Please make a selection: 
            1. Applications
            2. Linux Apps/packages
            """ + '\n')
        if int(linux_tools_submenu) == 1:
            linux_apps = input("""Please make a selection: 
            1. Input Remapper
            2. Discord
            3. Plex
            """ + '\n')
            if int(linux_apps) == 1:
                #add installer for input remapper
                command = "sudo ./input_remapper/input_remapper_fix.sh"
                send_command(linux_apps,command)

                print('test')
            elif int(linux_apps) == 2:
                command = "sudo snap install discord"
                send_command(linux_apps,command)
                
                linux_apps = input("""Please make a selection: 
                1. Input Remapper
                2. Discord
                3. Plex
                """ + '\n')
            
            
        else:
            linux_tools_submenu = input("""Please make a selection: 
            1. Howdy reinstallation

            """ + '\n')

            if int(linux_tools_submenu) == 1:    
                howdy_install = """cd ./tmp && sudo ../howdy/fix_howdy.sh && sudo rm -f ./*"""
                result1 = subprocess.run(howdy_install, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                # Get the output and error (if any)
                output1 = result1.stdout
                error1 = result1.stderr
                        # Check if the command was successful
                if result1.returncode == 0:
                    print("Command executed successfully!")
                    print("Output:\n", output1)
                else:
                    print("Command failed with return code:", result1.returncode)
                    if error1:
                        print("Error:\n", error1)
                    else:
                        print('test')
                    
        
                    
else:
    kernel_path = str(input("""Please give the path to the kernel zip: """))
    extract_dir = str(os.getcwd())
    #command = "./build_kernel.sh"
    command1 = """tar -xvf {} ; extracted_folder_name=$(basename "${}") ; sudo cp /boot/config-`uname -r` ./$extracted_folder_name/.config  """.format(kernel_path, kernel_path,'linux-')
    #command2 = "extracted_folder_name=$(basename "${}" .tar.xz && sudo cp /boot/config-`uname -r` ./$extracted_folder_name\.config".format(kernel_path)
    
    result1 = subprocess.run(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Get the output and error (if any)
    output1 = result1.stdout
    error1 = result1.stderr


    # Check if the command was successful
    if result1.returncode == 0:
        print("Command executed successfully!")
        print("Output:\n", output1)
    else:
        print("Command failed with return code:", result1.returncode)
        if error1:
            print("Error:\n", error1)
    """        
    if result2.returncode == 0:
        print("Command executed successfully!")
        print("Output:\n", output2)
    else:
        print("Command failed with return code:", result2.returncode)
        if error:
            print("Error:\n", error2)
    """
                
        