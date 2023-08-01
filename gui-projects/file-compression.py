import PySimpleGUI as pg
from zip_creator import make_archive

label1 = pg.Text("Select Files to Compress: ")
input1 = pg.Input()
button1 = pg.FilesBrowse("Choose", key="files")

label2 = pg.Text("Select Destination Folder: ")
input2 = pg.Input()
button2 = pg.FolderBrowse("Choose", key="destinations")
compress_button = pg.Button("Compress")
output_label = pg.Text(key="output_txt")


window = pg.Window("File Compressor", layout=[[label1, input1, button1], [label2,input2,button2], [compress_button, output_label]])
#display window

while True:
    event, values = window.read()
    print(event, values)
    filepath = values["files"].split(";")
    destination = values["destinations"]
    make_archive(filepath, destination)
    window["output_txt"].update(value="compression completed")

window.close()
