import shutil
import webbrowser
from tkinter import Tk, Canvas, PhotoImage, YES, Entry, Label, Button, filedialog
from moviepy.editor import VideoFileClip
from pytube import YouTube


# fonksyon

def open_youtube():
    webbrowser.open_new("https://www.youtube.com")


def select_path():
    # Permet itilizate a chwazi path nan explorer an
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # Recuperer path user a choisi an
    get_lyen = chwazi_lyen.get()
    # Recuperer lien video a telecharger an
    user_path = path_label.cget("text")
    fenet.title('Downloading...')

    # Telecharger video a
    mp4_video = YouTube(get_lyen).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()

    # Deplacer video a nan avek module shutil.move
    shutil.move(mp4_video, user_path)
    fenet.title('Download Complete! Download another file...')


# kreyasyon yon fenet
fenet = Tk()

# Pesonalize fenet la
fenet.title("Youtube Video Downloader")
# Tay pa defo fenet lan
fenet.geometry("720x480")
# tay minimal pou fenet la genyen
fenet.minsize(480, 420)
# Ajoute icon nan tet fenet la
fenet.iconbitmap("ytd_.ico")
# Ajoute koule background nan fenet la
fenet.config(background='#ededed')

canvas = Canvas(fenet, width=500, height=500, bg='#ededed', bd=0, highlightthickness=0)
canvas.pack(expand=YES)

# Image logo
logo_imaj = PhotoImage(file='yt.png')

# Redimansyone imaj
logo_imaj = logo_imaj.subsample(2, 2)

# Ajoute imaj lan nan canvas
canvas.create_image(250, 80, image=logo_imaj)

# =======================================================

# Kreyasyon bouton pou itilizate a visite youtube
yt_btn = Button(fenet, text='Visit youtube', font=('Courrier', 10), bg='#c72222', fg='white', command=open_youtube)
canvas.create_window(250, 160, window=yt_btn)

# Kreyasyon champ yo --> champ lyen
chwazi_lyen = Entry(fenet, width=50)
lyen_label = Label(fenet, text='Entrer Download Link', font=('Courrier', 16), bg='#ededed')

# Ajoute lien_label nan fenet la
canvas.create_window(250, 200, window=lyen_label)
canvas.create_window(250, 230, window=chwazi_lyen)

# Seleksyone kote wap anregistrer fichye a
path_label = Label(fenet, text='Select Path for Download', font=('Courrier', 16), bg='#ededed')
bouton_select = Button(fenet, text='Select path', command=select_path, bg='#c72222', fg='white', font=('Courrier', 10))

# Ajoute Sa yo nan fenet la
canvas.create_window(250, 300, window=path_label)
canvas.create_window(250, 350, window=bouton_select)

# Kreyasyon bouton download
download_btn = Button(fenet, text='Download File', command=download_file, bg='#c72222', fg='white',
                      font=('Courrier', 10))
# Ajoute bouton download lan nan Canvas
canvas.create_window(250, 400, window=download_btn)

# ===========================================================

# Afichaj fenet la
fenet.mainloop()
