import tkinter as tk
from tkinter import ttk, messagebox
import pyshorteners
from tkinter import font as tkfont

class URLShortenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")
        
        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#2196F3")
        style.configure("TEntry", padding=6)
        
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
        title_label = ttk.Label(
            main_frame,
            text="URL Shortener",
            font=title_font
        )
        title_label.pack(pady=(0, 20))
        
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.url_entry = ttk.Entry(
            input_frame,
            width=50,
            font=("Helvetica", 12)
        )
        self.url_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        shorten_button = ttk.Button(
            input_frame,
            text="Shorten URL",
            command=self.shorten_url,
            style="TButton"
        )
        shorten_button.pack(side=tk.LEFT)
        
        result_frame = ttk.Frame(main_frame)
        result_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.result_entry = ttk.Entry(
            result_frame,
            width=50,
            font=("Helvetica", 12),
            state="readonly"
        )
        self.result_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        copy_button = ttk.Button(
            result_frame,
            text="Copy",
            command=self.copy_to_clipboard,
            style="TButton"
        )
        copy_button.pack(side=tk.LEFT)
        
        self.status_label = ttk.Label(
            main_frame,
            text="",
            font=("Helvetica", 10)
        )
        self.status_label.pack(pady=(10, 0))
        
        self.shortener = pyshorteners.Shortener()
    
    def shorten_url(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return
        
        try:
            short_url = self.shortener.tinyurl.short(url)
            self.result_entry.configure(state="normal")
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, short_url)
            self.result_entry.configure(state="readonly")
            self.status_label.configure(text="URL shortened successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to shorten URL: {str(e)}")
            self.status_label.configure(text="Error occurred while shortening URL")
    
    def copy_to_clipboard(self):
        short_url = self.result_entry.get()
        if short_url:
            self.root.clipboard_clear()
            self.root.clipboard_append(short_url)
            self.status_label.configure(text="Copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No shortened URL to copy")

def main():
    root = tk.Tk()
    app = URLShortenerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 