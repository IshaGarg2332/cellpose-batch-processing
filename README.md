Cellpose_run.py
- It runs the Cyto2 custom model on all images for one mouse at one time
1. It searches a folder for image files that have “c1” in their name
2. The code loads a pretrained model from a file on your computer
3. In this case, it is Cyto2 custom model
4. For every “c1” file, it opens the image so the model can analyze it
5. The model tries to find all masks in the image
6. For each processed image, it saves three things: a _seg.npy, a _cp_masks.png, and a copy of the original c1 image
7. Then it repeats for all FOV or any type of subfolders within the larger mouse folder

updatecells1.py
- After adding and removing masks, it edits the seg.npy and cp_masks.png files
- It creates a document with the number of masks made by the model, the number of masks made manually, and the total number of masks
1. Goes inside the folder given and sorts all the FOV folders or other subfolders in numerical order
2. Then it sorts all images in the FOV folders in order based on the number in the name
3. Inside each folder, it looks for files ending with _seg.npy
4. It opens each _seg.npy file, checks if it has a masks entry, and then converts the mask data into an image
5. It saves this image as a _cp_masks.png file
6. It creates a .docx file and adds a heading for each folder (every FOV)
7. Inside each folder section, it creates a table with columns:
       - File Name - Name of the image
       - Model Masks - Amount of masks made by the Cyto2 custom model
       - Manual Masks - Amount of masks made manually afterwards
       - Total Masks - Total masks in the end

copyc2.py
- It copies all c2 files from the original folder into the new folder that was made and analyzed
1. Goes through every file in the original folder given
2. It checks if the file has the words “c2” in the name or not
3. If the file contains “c2” in its name, the code copies the image into the matching output folder
4. BUT, it only copies the file if it doesn’t already exist there
