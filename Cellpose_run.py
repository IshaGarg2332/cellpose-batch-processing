import numpy as np
import os
import sys
import shutil
from cellpose import models, io

def run_cellpose_on_c1_files(input_folder, output_folder, model_path, model=None):
    if model is None:
        model = models.CellposeModel(gpu=False, pretrained_model=model_path)

    os.makedirs(output_folder, exist_ok=True)

    all_files = os.listdir(input_folder)
    c1_files = [f for f in all_files if 'c1' in f.lower()]
    print(f"Found {len(c1_files)} 'c1' files to process in {input_folder}")

    for idx, file_name in enumerate(c1_files, start=1):
        file_path = os.path.join(input_folder, file_name)

        imgs = io.imread(file_path)
        masks, flows, styles = model.eval(imgs, diameter=15.59, channels=[0, 0], normalize=True, resample=True)

        base_name = os.path.splitext(file_name)[0]
        npy_path = os.path.join(output_folder, f"{base_name}")
        png_path = os.path.join(output_folder, f"{base_name}")
        copied_image_path = os.path.join(output_folder, file_name)

        io.masks_flows_to_seg(imgs, masks, flows, npy_path, channels=[0, 0])
        io.save_masks(imgs, masks, flows, png_path, png=True)
        shutil.copy2(file_path, copied_image_path)

        print(f"Completed file {file_name} ({idx}/{len(c1_files)})")

def batch_process_all_folders(root_input_dir, root_output_dir, model_path):
    model = models.CellposeModel(gpu=False, pretrained_model=model_path)

    # --- Process C1 files directly ---
    run_cellpose_on_c1_files(root_input_dir, root_output_dir, model_path, model)

    # --- Process subfolders ---
    for folder_name in os.listdir(root_input_dir):
        input_folder = os.path.join(root_input_dir, folder_name)
        output_folder = os.path.join(root_output_dir, folder_name)

        if os.path.isdir(input_folder):
            print(f"\nProcessing {folder_name}...")
            run_cellpose_on_c1_files(input_folder, output_folder, model_path, model)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python cellpose_run.py <root_input_dir> <root_output_dir>")
        sys.exit(1)

    root_input_dir = sys.argv[1]
    root_output_dir = sys.argv[2]

    model_path = r"C:\Users\gargi\Downloads\Cyto2 custom model" #NEEDS CHANGING
    batch_process_all_folders(root_input_dir, root_output_dir, model_path)
