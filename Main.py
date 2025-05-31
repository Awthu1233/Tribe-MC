import minecraft_launcher_lib as mc
import subprocess
from colorama import Fore


print(Fore.MAGENTA + "                                                   ***\\Welcome to Tribe MC!//***" )
print(Fore.MAGENTA + "                                                                V.0.1" )


mc_dir = mc.utils.get_minecraft_directory()
all_ver_info = mc.utils.get_available_versions(mc_dir)

ver_list = []
av_ver_list = []


def install_version():
    for version in all_ver_info:
        if version["type"] == "release":
            ver_list.append(version["id"])

    for index, version in enumerate(ver_list):
        print(index, version)

    version = int(input(Fore.YELLOW + " Which version do you want to install? "))
    mc.install.install_minecraft_version(ver_list[version], mc_dir)
    print(Fore.GREEN + "Version installed successfully!")


def launch_version():
    info = open("info.txt", "a")
    settings = {
        "username": input(Fore.CYAN + "Put your username: "),
        "uuid": "id",
        "token": "token"
    }

    info.write("name: " + settings["username"] + "\n")
    info.write("UUID: " + settings["uuid"] + "\n")
    info.write("Token: " + settings["token"] + "\n") 
    print(Fore.MAGENTA + "You can see your username, uuid and token in info.txt file.")   

    av_ver_list = []
    for index, version in enumerate(mc.utils.get_installed_versions(mc_dir)):
        print(index, version["id"])
        av_ver_list.append(version["id"])

    if not av_ver_list:
        print(Fore.RED + "None of the versions are installed.")
        print(Fore.RED + "Please install a version first.")
        return

    sel_ver = int(input(Fore.GREEN + "select a version to launch: "))

    minecraft_command = mc.command.get_minecraft_command(av_ver_list[sel_ver], mc_dir, settings)
    subprocess.run(minecraft_command)


def main():
    if input(Fore.YELLOW + "Want to install any version? [Y/N] ").upper() == "y".upper():
        install_version()

    launch_version()


if __name__ == "__main__":
    main()
