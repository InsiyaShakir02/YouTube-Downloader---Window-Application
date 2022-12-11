import tkinter as tk
from tkinter import filedialog, NW, messagebox
import tkinter.font as tkFont
from pytube import YouTube
import webbrowser


class App:

    def __init__(self, root):
        # setting title


        root.title("YouTube Downloader")
        # setting window size
        width = 916
        height = 524
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

        # create a toplevel menu
        menubar = tk.Menu(root)
        file = tk.Menu(menubar, tearoff=0)
        file.add_command(label="Open")
        file.add_command(label="Save")
        file.add_command(label="Save AS")
        file.add_command(label="Close")

        file.add_separator()
        file.add_command(label="Exit")

        # display the menu
        menubar.add_cascade(label="File", menu=file)

        edit = tk.Menu(menubar, tearoff=0)

        edit.add_command(label="Cut")
        edit.add_command(label="Copy")
        edit.add_command(label="Paste")
        edit.add_command(label="Delete")

        menubar.add_cascade(label="Edit", menu=edit)
        help = tk.Menu(menubar, tearoff=0)
        help.add_command(label="About Us")
        menubar.add_cascade(label="Help", menu=help)

        root.config(menu=menubar)
       

        self.video_audio_url = tk.StringVar()
        self.destinaton_path = tk.StringVar()
        self.filePath = ""
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root['bg'] = 'white'

        outer = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        outer["font"] = ft
        outer["fg"] = "#333333"
        outer["justify"] = "center"
        outer["text"] = ""
        outer["relief"] = "groove"
        outer.place(x=110, y=110, width=727, height=230)
        outer['bg'] = '#dde9f4'

        video_audio_url_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10, weight="bold")
        video_audio_url_label["font"] = ft
        video_audio_url_label["fg"] = "#333333"
        video_audio_url_label["justify"] = "center"
        video_audio_url_label["text"] = "Video/Audio url"
        video_audio_url_label.place(x=170, y=160, width=178, height=46)

        youtube_downloader_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=20, weight="bold")
        youtube_downloader_label["font"] = ft
        youtube_downloader_label["justify"] = "center"
        youtube_downloader_label["text"] = "YOUTUBE DOWNLOADER"
        youtube_downloader_label["relief"] = "groove"
        youtube_downloader_label.place(x=220, y=10, width=438, height=71)

        destination_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10, weight="bold")
        destination_label["font"] = ft
        destination_label["fg"] = "#333333"
        destination_label["justify"] = "center"
        destination_label["text"] = "Destination"
        destination_label.place(x=170, y=220, width=178, height=46)

        video_audio_url_textbox = tk.Entry(root)
        video_audio_url_textbox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        video_audio_url_textbox["font"] = ft
        video_audio_url_textbox["fg"] = "#333333"
        video_audio_url_textbox["justify"] = "center"
        video_audio_url_textbox["text"] = "Entry"
        video_audio_url_textbox["textvariable"] = self.video_audio_url
        video_audio_url_textbox.insert(0, "video url")
        video_audio_url_textbox.place(x=380, y=160, width=248, height=40)

        self.destination_textbox = tk.Entry(root)
        self.destination_textbox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.destination_textbox["font"] = ft
        self.destination_textbox["fg"] = "#333333"
        self.destination_textbox["justify"] = "center"
        self.destination_textbox["text"] = "Entry"
        self.destination_textbox["textvariable"] = self.destinaton_path
        self.destination_textbox.insert(0, "")
        self.destination_textbox.place(x=380, y=230, width=248, height=40)

        download_button = tk.Button(root)
        download_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10, weight="bold")
        download_button["font"] = ft
        download_button["fg"] = "black"
        download_button["justify"] = "center"
        download_button["text"] = "DOWNLOAD"
        download_button["relief"] = "raised"
        download_button.place(x=330, y=350, width=224, height=72)
        download_button["command"] = self.download_button_command
        download_button["bg"] = "#BCED91"

        browse_button = tk.Button(root)
        browse_button["bg"] = "#abcae4"
        ft = tkFont.Font(family='Times', size=10, weight="bold")
        browse_button["font"] = ft
        browse_button["fg"] = "black"
        browse_button["justify"] = "center"
        browse_button["text"] = "Browse"
        browse_button["relief"] = "raised"
        browse_button.place(x=650, y=230, width=130, height=41)
        browse_button["command"] = self.browse_button_command


        youtube_button = tk.Button(root)
        ft = tkFont.Font(family='Times', size=10, weight="bold")
        youtube_button["font"] = ft
        youtube_button["fg"] = "white"
        youtube_button["justify"] = "center"
        youtube_button.place(x=650, y=450, width=130, height=41)
        youtube_button["relief"] = "raised"
        youtube_button["command"] = self.openweb
        youtube_button["text"] = "YouTube"
        youtube_button["bg"] = "red"

    def openweb(self):
        result = messagebox.askokcancel("Redirect", "Redirecting to www.youtube.com",)
        try:
            if result:
                new = 1
                url = "https://www.youtube.com/"
                webbrowser.open(url, new=new)
            else:
                root.quit()

        except Exception as e:
            print(e)

    def download_button_command(self):
        print(self.video_audio_url.get())
        try:
            result = messagebox.askquestion("Confirm", "Are you sure you want to download ?")
            if result:
                yt_obj = YouTube(self.video_audio_url.get())
                yt_obj.streams.first().download(self.destinaton_path.get())
                filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

                filters.get_highest_resolution().download()
                messagebox.showinfo("Download", "Video Downloaded!")
                print("Successfully downloaded!")

        except Exception as e:
            print(e)

    def browse_button_command(self):
        filename = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
        self.destination_textbox.delete(0, "end")
        self.destination_textbox.insert(0, filename)
        self.filePath = filename



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
