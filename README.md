[![Download ffmpeg-assembler](https://img.shields.io/sourceforge/dt/ffmpeg-assembler.svg)](https://sourceforge.net/projects/ffmpeg-assembler/files/latest/download)Python 3.11 | for windows users | Beta 

```
███████╗███████╗███╗   ███╗██████╗ ███████╗ ██████╗      █████╗ ███████╗███████╗███████╗███╗   ███╗██████╗ ██╗     ███████╗██████╗ 
██╔════╝██╔════╝████╗ ████║██╔══██╗██╔════╝██╔════╝     ██╔══██╗██╔════╝██╔════╝██╔════╝████╗ ████║██╔══██╗██║     ██╔════╝██╔══██╗
█████╗  █████╗  ██╔████╔██║██████╔╝█████╗  ██║  ███╗    ███████║███████╗███████╗█████╗  ██╔████╔██║██████╔╝██║     █████╗  ██████╔╝
██╔══╝  ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══╝  ██║   ██║    ██╔══██║╚════██║╚════██║██╔══╝  ██║╚██╔╝██║██╔══██╗██║     ██╔══╝  ██╔══██╗
██║     ██║     ██║ ╚═╝ ██║██║     ███████╗╚██████╔╝    ██║  ██║███████║███████║███████╗██║ ╚═╝ ██║██████╔╝███████╗███████╗██║  ██║
╚═╝     ╚═╝     ╚═╝     ╚═╝╚═╝     ╚══════╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
```

# 🎬 Video Assembler

![Language](https://img.shields.io/badge/language-English-green.svg) ![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)

Vidize is a PyQt5 application that allows you to effortlessly merge multiple video files from a selected folder. The videos can be assembled in a random order or based on the order they are named. The application supports popular video formats, such as MP4, MOV, AVI, and MKV, and provides an intuitive and efficient user experience. The project documentation and support are powered by OpenAI's ChatGPT.

In release section you can download an executable ready to launch (portable) made for windows with pyinstaller.

It's a non-signed software because I prefer to save my money for real stuff, so it will be detected as a malware from bad anti-virus, you can still test on sandbox here  : https://www.virustotal.com/gui/home/upload 

Or compile it by yourself , I made a tutorial downside of this page.

![image](https://user-images.githubusercontent.com/92639080/229273465-7c59eaea-a574-4b87-b7cf-f36aa4c04cd6.png)


BTW, if you are searching for more desk tools to opmtimize your productivity you can also check those pages :

- A fast file remover (delete all files who have the same name in a selected folder including subfolder) : https://github.com/SECRET-GUEST/decimator
- An image sorter, but it's in french : https://github.com/SECRET-GUEST/trieur
- A powerful autoclicker : https://github.com/SECRET-GUEST/autoclicker

And there are more in tiny script (without graphical user interface but easy to use ) : https://github.com/SECRET-GUEST/tiny-scripts

## 🌟 Features

- **Intuitive interface**: Modern and easy-to-use graphical interface.
- **Multiple video formats**: Supports popular video formats like MP4, MOV, AVI, and MKV.
- **Flexible assembly options**: Assemble videos in a random order or by their names.
- **Customizable output**: Save the assembled video in the same folder or choose a different output folder.
- **Real-time progress**: Monitor the progress of the assembling process in a terminal-like interface.

## 🚀 Getting Started

1. Launch the application.
2. Click the "Select a folder" button to choose the folder containing the video files you want to merge.
3. If you want to save the assembled video in a different folder, uncheck the "Save in the same folder" checkbox and click the "Select output folder" button to choose the output folder.
4. Check or uncheck the "Assemble videos in a random order" checkbox according to your preference.
5. Click the "Start assembling" button to begin the merging process.
6. Monitor the progress of the assembling process in the terminal-like interface.


[![Download ffmpeg-assembler](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/ffmpeg-assembler/files/latest/download)


## :scroll: License

This repository is released under the [MIT License](LICENSE). Please see the `LICENSE` file for more information.

## :question: Support & Questions

If you have any questions or need support, please feel free to open an issue or join my twitter.





```
██   ██  ██████  ██     ██     ████████  ██████      ██████  ██    ██ ███    ██ 
██   ██ ██    ██ ██     ██        ██    ██    ██     ██   ██ ██    ██ ████   ██ 
███████ ██    ██ ██  █  ██        ██    ██    ██     ██████  ██    ██ ██ ██  ██ 
██   ██ ██    ██ ██ ███ ██        ██    ██    ██     ██   ██ ██    ██ ██  ██ ██ 
██   ██  ██████   ███ ███         ██     ██████      ██   ██  ██████  ██   ████ 
```

Here's a tutorial explaining different ways to run the files:

# For **MAC** & **Linux** users:

Since this script is designed for Windows users, you should probably first improve the code.

However, here is the procedure to run the script:

* :computer:: [MAC] - https://macosx-faq.com/how-to-run-python-script/
* :keyboard: [LINUX] - open a terminal, then `cd` to the script's directory and type:

```
python script.pyw

```
(where `script.pyw` is obviously the name of the file you've downloaded)

# :desktop_computer: For **Microsoft** users:

Because this script is made by PyInstaller, it could be detected as malware. (sorry, but I will not spend money to just be approved by "security" software/websites, you have the code, and here are possibilities to help you run it:

## :large_orange_diamond: 1. Run by simple click on `APPLICATION.exe`

The `.exe` file is a portable version created for Microsoft users with PyInstaller, allowing you to download and use this file alone, without any additional files.

If there is no `.exe` file available, it means that the application is stored in a directory, as a portable version is not provided. In this case, simply locate the `APP_NAME.exe` file within the directory and launch it with a single click. You can place the folder anywhere you like and create a shortcut to the executable file for easy access.

## :large_orange_diamond: 2. Run with Python

`Python script` is a directory with the original script for python 3.11.

In case you have a lower version, you may have to download module imported not included with your version. Just read the first lines of the script in Alexandria with a notepad or whatever to find what's missing.

If you would like to run with python **YOU WILL NEED THE IMAGE .png PLACED IN THE SAME DIRECTORY OF THE RUNNING SCRIPT**.

Also, you can add a `w` to the extension (like `script.pyw`). It means `windowed mode`, to launch the python script without the CMD, but it's still a common python file.

## :large_orange_diamond: 3. Compile the script by yourself

### :gear: Instructions :gear: 

To create your own executable from the python file, you will need to install pyinstaller and python.

Here are the steps you should follow:

   :small_red_triangle: Download python 3.11.1 

Don't forget to add it to your path with the installer or in variables environment (so reboot your PC after the installation), here is the link: 

:crossed_flags: https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe :crossed_flags:

:small_red_triangle: Open your CMD as an administrator and type the following command:

```
python -m pip install pyinstaller
```

:small_red_triangle: You can now run it using a ruby `.spec` file by entering the following command in the project directory:

```bash
pyinstaller YOUR_FILE.spec
```
Normally, I place a blank.spec file in the "script" folder, if there isn't one let's watch over here:

:crossed_flags: https://github.com/SECRET-GUEST/tiny-scripts/tree/ALL/useful%20for%20python/pyinstaller :crossed_flags:

:small_red_triangle: You can also run it directly with your OS, type the following command, replacing the file paths with your own:

```
pyinstaller --onefile --icon="...YOUR PATH.../YOUR ICON.ico" --add-data "...YOUR PATH.../ico;ico" --noconsole test.py
```
#### Here are the explanations of the different options:



- `--onefile`: creates a single executable that includes all dependencies.

- `--icon=icon.ico`: specifies the icon to use for the executable (replace icon.ico with the path to your icon file).

- `--add-data "path/to/file;folder_name"`: adds external files required by the program. The path to the file and the name of the folder in which the file will be extracted should be separated by a semicolon `;`. You can add multiple files by separating them with semicolons.

- `script.py`: specifies the name of your Python script.

- `--noconsole`: hides the console when the executable is run.



Make sure to replace the snipped parts with the names of your files and folders. Also note that the path should be specified based on the operating system you are working on.

After running this command, you should have a single executable that includes all dependencies, external files, and a custom icon, and does not show the console when running.

Alternatively, you can also :

## :large_orange_diamond: 4. Create a batch file to run

- [ ] Create a text file

- [ ] In the text file type and write (and change/complete the path, first is for python, 2nd is for script.py):

```
C:\YOUR PATH TO PYTHON\python.exe" "C:\**YOUR PATH TO THE SCRIPT**\script.pyw"
```


If Python is in the path, you can just:

```
python "C:\**YOUR PATH TO THE SCRIPT**\script.pyw"
```

- [ ] Rename the `new_file.txt` to `script.bat` then just click on it, and it will run the program


```
     _ ._  _ , _ ._            _ ._  _ , _ ._    _ ._  _ , _ ._      _ ._  _ , _ .__  _ , _ ._   ._  _ , _ ._   _ , _ ._   .---.  _ ._   _ , _ .__  _ , _ ._   ._  _ , _ ._      _ ._  _ , _ .__  _ , _ . .---<__. \ _
   (_ ' ( `  )_  .__)        (_ ' ( `  )_  .__ (_ ' ( `  )_  .__)  (_ '    ___   ._( `  )_  .__)  ( `  )_  .__)   )_  .__)/     \(_ ' (    )_  ._( `  )_  .__)  ( `  )_  .__)  (_ ' ( `  )_  ._( `` )_  . `---._  \ \ \
 ( (  (    )   `)  ) _)    ( (  (    )   `)  ) (  (    )   `)  ) _ (  (   (o o) )     )   `)  ) _    )   `)  ) _    `)  ) \.@-@./(  (    )   `)     )   `)  ) _    )   `)  ) _ (  (    )   `)         `) ` ),----`- `.))  
(__ (_   (_ . _) _) ,__)  (__ (_   (_ . _) _) _ (_   (_ . _) _) ,__ (_   (  V  ) _) (_ . _) _) ,_  (_ . _) _) ,_ . _) _) ,/`\_/`\ (_   (  . _) _) (_ . _) _) ,_  (_ . _) _) ,__ (_   (_ . _) _) (__. _) _)/ ,--.   )  |
    `~~`\ ' . /`~~`           `~~`\ ' . /`~~`   `~~`\ ' . /`~~`     `~~`/--m-m- ~~`\ ' . /`~~`   `\ ' . /`~~`  `\ ' . /  //  _  \\ ``\ '  . /`~~`\ ' . /`~~`   `\ ' . /`~~`     `~~`\ ' . /`~~`\ ' . /`~~/_/    >     |
         ;   ;                     ;   ;             ;   ;               ;   ;      ;   ;          ;   ;         ;   ;  | \     )|_   ;    ;      ;   ;          ;   ;               ;   ;      ;   ;    |,\__-'      |
         /   \                     /   \             /   \               /   \      /   \          /   \         /   \ /`\_`>  <_/ \  /    \      /   \          /   \               /   \      /   \     \__         \
________/_ __ \___________________/_ __ \___________/_ __ \______ __ ___/_ __ \____/_ __ \________/_ __ \_______/_ __ \\__/'---'\__/_/_  __ \____/_ __ \________/_ __ \_____ _______/_ __ \____/_ __ \____ __\___      )
```


