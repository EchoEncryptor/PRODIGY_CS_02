import argparse
import random
from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def generate_permutation(length, key):
    rnd = random.Random(key)
    perm = list(range(length))
    rnd.shuffle(perm)
    return perm

def invert_permutation(perm):
    inv = [0] * len(perm)
    for i, p in enumerate(perm):
        inv[p] = i
    return inv

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    arr = np.array(img)
    shape = arr.shape

    if arr.ndim == 3:
        flat = arr.reshape(-1, shape[2])
    else:
        flat = arr.flatten()

    length = flat.shape[0]
    perm = generate_permutation(length, key)
    flat_permuted = flat[perm]
    flat_enc = (flat_permuted + key) % 256
    arr_enc = flat_enc.reshape(shape)

    enc_img = Image.fromarray(arr_enc.astype('uint8'))
    enc_img.save(output_path)

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    arr = np.array(img)
    shape = arr.shape

    if arr.ndim == 3:
        flat = arr.reshape(-1, shape[2])
    else:
        flat = arr.flatten()

    flat_dec = (flat - key) % 256
    length = flat_dec.shape[0]
    perm = generate_permutation(length, key)
    inv_perm = invert_permutation(perm)
    flat_orig = flat_dec[inv_perm]

    arr_orig = flat_orig.reshape(shape)
    orig_img = Image.fromarray(arr_orig.astype('uint8'))
    orig_img.save(output_path)

# ================= GUI ===================
def browse_input():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, path)

def browse_output():
    path = filedialog.asksaveasfilename(defaultextension=".png",
                                        filetypes=[("PNG Image", "*.png"), ("All Files", "*.*")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, path)

def process_image():
    input_path = input_entry.get()
    output_path = output_entry.get()
    key_text = key_entry.get()
    mode = mode_var.get()

    if not input_path or not output_path or not key_text:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    try:
        key = int(key_text)
    except ValueError:
        messagebox.showerror("Input Error", "Key must be an integer.")
        return

    try:
        if mode == "Encrypt":
            encrypt_image(input_path, output_path, key)
            messagebox.showinfo("Success", "Image encrypted successfully!")
        else:
            decrypt_image(input_path, output_path, key)
            messagebox.showinfo("Success", "Image decrypted successfully!")
    except Exception as e:
        messagebox.showerror("Processing Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Image Encryption Tool")
root.geometry("450x300")
root.resizable(False, False)

ttk.Label(root, text="Input Image:").pack(pady=(10, 0))
input_frame = ttk.Frame(root)
input_frame.pack()
input_entry = ttk.Entry(input_frame, width=40)
input_entry.pack(side=tk.LEFT, padx=(0, 5))
ttk.Button(input_frame, text="Browse", command=browse_input).pack(side=tk.LEFT)

ttk.Label(root, text="Output Image:").pack(pady=(10, 0))
output_frame = ttk.Frame(root)
output_frame.pack()
output_entry = ttk.Entry(output_frame, width=40)
output_entry.pack(side=tk.LEFT, padx=(0, 5))
ttk.Button(output_frame, text="Browse", command=browse_output).pack(side=tk.LEFT)

ttk.Label(root, text="Key (integer):").pack(pady=(10, 0))
key_entry = ttk.Entry(root, width=20)
key_entry.pack()

mode_var = tk.StringVar(value="Encrypt")
ttk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt").pack()
ttk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt").pack()

ttk.Button(root, text="Run", command=process_image).pack(pady=15)

root.mainloop()
