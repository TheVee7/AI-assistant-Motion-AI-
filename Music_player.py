import os 
import random
import vlc
import time
import threading

def play_random_songs(directory, num_songs):
    files = os.listdir(directory)
    mp3_files = [file for file in files if file.endswith(".mp3")]

    if len(mp3_files) < num_songs:
        print("Not enough MP3 files in the directory.")
        return

    songs_to_play = random.sample(mp3_files, num_songs)

    instance = vlc.Instance('--no-video')  # Create VLC instance without video output
    global player
    player = instance.media_player_new()   # Create media player
    
    for song in songs_to_play:
        print("Playing:", song)
        media = instance.media_new(os.path.join(directory, song))
        player.set_media(media)

        # Play the song
        player.play()

        # Wait for the song to finish playing
        while player.get_state() != vlc.State.Ended:
            time.sleep(1)
    
    player.release()  # Release the player resources

def control(action):
    if action == "stop":
        player.pause()
    elif action == "next":
        player.stop()
        directory = "E:\\MUSIC"
        num_songs = 5
        threading.Thread(target=play_random_songs, args=(directory, num_songs)).start()

directory = "E:\\MUSIC"
num_songs = 5
threading.Thread(target=play_random_songs, args=(directory, num_songs)).start()
