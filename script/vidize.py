#     |               |                                 |
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  |                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    |
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                                                        |
#     |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                       |                    |
                
#                     |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#          |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                |                                        |
                
#                 |                     |
#  |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |     |                                |                       |                              |                                |
#          |                               |                                         |                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#  |         |                                   PRESENTATION                                                |                                |                    |   |                                |                    |   |                                |                    |        |                                |                    |
#                                                                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#               |                             /                 \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#       |                               This tools permit to assemble 
                
#                               multiple footages in random or regular order.                  |                                           |               |                                           |               |                                           |                    |                                           |
                
#                          /                      |    v    |                    \
                
#                  The program is using ffmpeg and show the cmd returns in a text file      |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |
#                                                                                                   |                                                                 |                      |                     |                       |                      |                     |                       |                      |                     |                            |
#      initially made in adding of an animation script for blender maybe it will evolve in the future

# You can say thank you OpenAI for this software, developped by GPT-4 under my direction, too poinless to do solo
#     |                  !      |                                   |     |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
#                               |                                   |     |                  
#                  |            |                   Anyway          !                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |
                
#             |                      |                 have                                                 |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                                           |
                

#                |                                  FUN         |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                                                      |
                
#                                                        =)
                
#
#                               |                      or                                       |                                                            |                    |                |                       |                    |                |                       |                    |                    |                                           |
                

#             |                              |       DIE ! ! !        |                       |                            |                |                       |                    |                |                       |                    |                    |                                           |#     |                        |                                         |                                |
                
#
#                                                    !                                       |                                |                    |  |                                |                    |  |                                |                    |       |                                |                    |
                
#     |               |                                 !
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  !                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    !
            
#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|
         


import os,sys,random,shutil,ffmpeg,tempfile,subprocess
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QCheckBox, QMessageBox, QTextEdit)




#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                

#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3


#function to make an exe file with py to exe
def ressource_path(relative_path):
    try:
        base_path=sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path ,relative_path)
#to make it works, you have to rename all your path with ressource_path (/path/) WHEN YOU WILL TURN THE SCRIPT TO EXE
#Example : /icon/lol.png  BECOME  ressource_path(/icon/lol.png)




#____ _  _ ___     ____ ____ ___  _    _ ____ ____ _  _ ___ 
#|    |\/| |  \    |__/ |___ |__] |    | |    |__| |\ |  |  
#|___ |  | |__/    |  \ |___ |    |___ | |___ |  | | \|  |  

                                                  

#This software is made with GPT-4 under my direction so say thank you open A.I.



class AssembleThread(QThread):
    update_terminal = pyqtSignal(str)
    error_occurred = pyqtSignal(str)

    def __init__(self, folder_path, output_folder):
        super().__init__()
        self.folder_path = folder_path
        self.output_folder = output_folder
        self.success = False 

    def run(self):
        self.assemble_videos(self.folder_path, self.output_folder, self.random_order)

    # Assemble videos using FFmpeg
    def assemble_videos(self, folder_path, output_folder, random_order=True):

        # Check if the video has an audio stream
        def has_audio_stream(video_file):
            try:
                probe = ffmpeg.probe(video_file)
                for stream in probe['streams']:
                    if stream['codec_type'] == 'audio':
                        return True
                return False
            except ffmpeg.Error as e:
                return False

        # Get all video files in the folder
        video_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.mp4', '.mov', '.avi', '.mkv'))]


        # Shuffle the videos if random order is selected
        if random_order:
            random.shuffle(video_files)
        else:
            video_files.sort()


        # Convert the videos to MP4 without loss
        temp_files = []
        temp_dir = tempfile.mkdtemp()
        try:
            concat_file = tempfile.mktemp(dir=temp_dir, suffix='.txt')
            with open(concat_file, 'w') as concat_f:
                for f in video_files:
                    input_path = os.path.join(folder_path, f)
                    temp_file = tempfile.mktemp(dir=temp_dir, suffix='.mp4')
                    temp_files.append(temp_file)

                    # FFmpeg command to convert videos with audio
                    if has_audio_stream(input_path):
                        command = ['ffmpeg', '-i', input_path, '-c:v', 'libx264', '-crf', '18', '-c:a', 'aac', '-strict', 'experimental', '-r', '30', '-vf', 'scale=-1:720', '-ar', '44100', '-ac', '2', temp_file]

                    # FFmpeg command to convert videos without audio
                    else:
                        command = ['ffmpeg', '-i', input_path, '-c:v', 'libx264', '-crf', '18', '-c:a', 'aac', '-strict', 'experimental', '-f', 'lavfi', '-i', 'anullsrc', '-shortest', '-r', '30', '-vf', 'scale=-1:720', '-ar', '44100', '-ac', '2', temp_file]

                    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, creationflags=subprocess.CREATE_NO_WINDOW)

                    for line in process.stdout:
                        self.update_terminal.emit(line.strip())

                    concat_f.write(f"file '{temp_file}'\n")

            # Assemble the videos with FFmpeg
            output_name = ''.join([os.path.splitext(f)[0] for f in video_files]) + '.mp4'
            output_path = os.path.join(output_folder, output_name)

            command = ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', concat_file, '-c', 'copy', output_path]
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, creationflags=subprocess.CREATE_NO_WINDOW, shell=True)


            for line in process.stdout:
                self.update_terminal.emit(line.strip())

            # Remove temporary files
            for temp_file in temp_files:
                os.remove(temp_file)
            os.remove(concat_file)
            shutil.rmtree(temp_dir)

           
            self.success = True

        except Exception as e:
            self.error_occurred.emit(f"An error occurred while assembling the videos: {e}")
            # Remove temporary files in case of an error
            for temp_file in temp_files:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)




#____ _  _ _    ___  ____ ____ ____ ____ ____ _  _ 
#| __ |  | |    |__] |__/ |  | | __ |__/ |__| |\/| 
#|__] |__| |    |    |  \ |__| |__] |  \ |  | |  | 


class VideoAssembler(QWidget):
    def __init__(self):
        super().__init__()


        self.init_ui()


    # Initialize UI elements
    def init_ui(self):

        self.setWindowIcon(QIcon(ressource_path("ico/vidize.png")))

        #Style of the whole application (css)
        self.setStyleSheet("""
            QWidget {
                background-color: #B0F2B4;
                color: #023047;
                font-family: "Comic Sans MS";
            }

            

            QMessageBox{
                background-color: #B0F2B4;
                color: #023047;
                font-family: "Comic Sans MS";
            }



            QCheckBox::indicator {
                border: 0.5px solid #023047;
                border-radius: 50%; 
                width: 10px;
                height: 10px;
            }

            QCheckBox::indicator:checked {
                background-color: #023047;
                border-color: #023047;
            }

            QCheckBox::indicator:hover {
                border-color: #F2E2BA;
            }

            QCheckBox::indicator:checked:hover {
                background-color: #F2E2BA;
                border-color: #F2E2BA;
            }

            QCheckBox::indicator:disabled {
                border-color: #B0F2B4;
                background-color: #B0F2B4;
            }

            



            QTextEdit {
                background-color: black;
                color: lime;
                font-family: 'Cascadia Code SemiBold';
                font-size: 10pt;
                border: 1px solid lime;
            }

            QScrollBar:vertical {
                background: #023047;
                width: 12px;
                margin: 0px;
            }

            QScrollBar::handle:vertical {
                background: #B0F2B4;
                min-height: 20px;
            }

            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }

            


            
            QPushButton {
                background-color: #F2E2BA;
                color: #023047;
                border-top-right-radius: 10px;
                border-bottom-left-radius: 10px;
                padding: 5px 10px;
            }
            
            QPushButton:hover {
                background-color: #c7baf2;
            }
            
            QPushButton:pressed {
                background-color: #A0E2A4;
            }
            
                       

            QMessageBox QHeaderView::section, QMainWindow QHeaderView::section, QDockWidget QHeaderView::section {
                background-color: #B0F2B4;
                color: #023047;
            }
            """)
        
    
        self.label = QLabel("No folder selected", self)
        self.button = QPushButton("Select a folder", self)
        self.button.clicked.connect(self.select_folder)

        self.checkbox = QCheckBox("Save in the same folder", self)
        self.checkbox.setChecked(True)

        self.output_button = QPushButton("Select an output folder", self)
        self.output_button.clicked.connect(self.select_output_folder)
        self.output_button.hide()

        self.start_button = QPushButton("Start assembling", self)
        self.start_button.clicked.connect(self.start_assembling)
        self.start_button.hide()


        self.random_checkbox = QCheckBox("Assemble videos in random order", self)
        self.random_checkbox.setChecked(True)

        self.checkbox.stateChanged.connect(self.toggle_output_button)

        self.terminal = QTextEdit(self)
        self.terminal.setReadOnly(True)
        self.terminal.setStyleSheet("")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.output_button)
        layout.addWidget(self.start_button)
        layout.addWidget(self.random_checkbox)
        layout.addWidget(self.terminal)

        self.setLayout(layout)
        self.setWindowTitle("Video Assembler")

    def toggle_output_button(self):
        if self.checkbox.isChecked():
            self.output_button.hide()
        else:
            self.output_button.show()

    # Select a folder containing video files
    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select a folder")
        if folder_path:
            self.label.setText(f"Folder selected: {ressource_path(folder_path)}")
            self.folder_path = folder_path
            self.start_button.show()

    # Select an output folder for the assembled video
    def select_output_folder(self):
        self.output_folder = QFileDialog.getExistingDirectory(self, "Select an output folder")

    # Start the video assembly process
    def start_assembling(self):
        if self.checkbox.isChecked():
            output_folder = self.folder_path
        else:
            output_folder = self.output_folder

        self.assemble_thread = AssembleThread(self.folder_path, output_folder)
        self.assemble_thread.random_order = self.random_checkbox.isChecked()
        self.assemble_thread.update_terminal.connect(self.update_terminal)
        self.assemble_thread.finished.connect(self.on_assemble_finished)
        self.assemble_thread.error_occurred.connect(self.on_assemble_error)

        self.assemble_thread.start()

    # Update the terminal with messages from the assembly process
    def update_terminal(self, message):
        self.terminal.append(message.strip())

    # Display a success message when assembly is complete
    def on_assemble_finished(self):
        if self.assemble_thread.success: 
            QMessageBox.information(self, "Success", "The videos have been successfully assembled.")

    # Display an error message if an error occurs during assembly
    def on_assemble_error(self, error_message):
        QMessageBox.critical(self, "Error", error_message)



#____ ____ ____ _  _ ____ ___    _    ____ _  _ _  _ ____ _  _
#|__/ |  | |    |_/  |___  |     |    |__| |  | |\ | |    |__|
#|  \ |__| |___ | \_ |___  |     |___ |  | |__| | \| |___ |  |
                
#ENDING | https://www.youtube.com/watch?v=CgZVrvQZB6U&ab_channel=SECRETGUEST :3


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VideoAssembler()

    window.show()
    sys.exit(app.exec_())

