import os, shutil, time
import tkinter as tk
import tkinter.font as tkFont

source = r"C:\Users\HP\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalState\shared\transfers"
dest_map = {
    ".docx": r"G:\My Drive\Docs",
    ".xlsx": r"G:\My Drive\Sheets",
    ".pptx": r"G:\My Drive\ppt",
    ".pdf":r"G:\My Drive\pdf"
}

seen = set()

while True:
    for directory, dirs, files in os.walk(source):
        for f in files:
            src = os.path.join(directory, f)
            if src not in seen:  # new file
                ext = os.path.splitext(f)[1].lower()
                if ext in dest_map:
                    dst = os.path.join(dest_map[ext], f)
                    shutil.move(src, dst)

                    root = tk.Tk()
                    root.overrideredirect(True)   # removes window borders
                    root.geometry("+1200+80")       # position at top-left corner
                    root.attributes("-topmost", True)  # keep on top
                    root.attributes("-transparentcolor", "white")  # make white fully transparent

                    # Create a label with white background (which will be transparent)
                    custom_font= tkFont.Font(family="Calibri Light", size=15, weight="normal")
                    label = tk.Label(root, text=f"Moved {f} → {dst}", font=custom_font, bg="white", fg="#00FFFF")
                    label.pack()

                    # Auto-close after 3 seconds
                    root.after(3000, root.destroy)
                    root.mainloop()

##                    print(f"Moved {f} → {dst}")
                seen.add(src)
    time.sleep(5)  # check every 5 seconds