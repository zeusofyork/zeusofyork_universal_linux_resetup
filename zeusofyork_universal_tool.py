import lzma
import os
import subprocess


'''
def decompress_xz_file(kernel_path, output_folder):
    # Make sure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Extract the file name (without extension) from the xz path
    file_name = os.path.basename(kernel_path).replace('.xz', '')
    
    # Full path for the decompressed file
    decompressed_file_path = os.path.join(output_folder, file_name)

    with lzma.open(kernel_path, 'rb') as f:
        with open(decompressed_file_path, 'wb') as decompressed_file:
            decompressed_file.write(f.read())
'''



menu = input("""Please select from the following options: 
    1. Linux
    2. Windows
    3. Android""" + '\n')


if int(menu) == 1:
    linux_tools = input("""Which tools? 
        1. Linux re-installation tools
        2. Kernel Builder
        """)
    if int(linux_tools) == 1:
        linux_tools_submenu = input("""Which tool?: 
        1. Kernel Builder
        2. Howdy reinstallation
        """ + '\n')
        if int(linux_tools_submenu) == 2:
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
                    
                    
                    
    elif int(linux_tools) == 2:
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
                
        

    else:
        print('test')

else:
    print("goodbye")

