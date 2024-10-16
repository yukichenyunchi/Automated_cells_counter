# Automated_cells_counter
Cells counting desktop application based on image processing.

# Use the code
There are two ways to use this project:
1. Dowload all the .py files in the same folder and run main.py with your own IDE.
2. Utilize pyinstaller package to pack all .py files into a exe file. Then, non-technical user can use the application by clicking the exe icon. 
For building multiple .py files into single.exe file, please refer to the references below. 

# Use the GUI
After running the code as described in previous section, there is a graphical user interface. The usage guide is as following:
1. Enter your diluent factor.
2. Upload an image of one of the 4 sets of 16 squares on hemocytometer. The image can be took by your phone through microscope eyes piece lens.
3. Crop the rectangle area that you want to count by dragging your mouse on the image.
4. Click count button and there is a pop out window to show counted cell. The user can check if the program work well manually.  
5. Close the pop out window and the calculated cells concentration is shown on the GUI.
   ![GUI_screen_shot](/GUI_screen_shot.png?raw=true)

# References
[Multiple .py files into single .exe](https://stackoverflow.com/questions/51455765/how-to-build-multiple-py-files-into-a-single-executable-file-using-pyinstaller)

[How to create rounded button in Tkinter?](https://stackoverflow.com/questions/42579927/how-to-make-a-rounded-button-tkinter)

[Crop an image on GUI](https://stackoverflow.com/questions/67762695/tkinter-draw-rectangle-using-a-mouse-and-crop-a-photo-in-the-shape-of-that-rec)

# Acknowledgement
Thank Dr. Chang, Ya-Jen (IBMS, Academia Sinica, Taiwan) for offering the biological materials in this project.






