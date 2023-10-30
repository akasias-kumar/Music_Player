import pygame

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
     pygame.mixer.music.stop()

def play_next_song(playlist, current_index):
    stop_music()
    next_index = (current_index + 1) % len(playlist)
    play_music(playlist[next_index])
    return next_index

if __name__ == "__main__":
    playlist = [
        "Deva_Shree_Ganesha.mp3",
        "Kitna_Kuch_Kehna_Hai.mp3",
        "Laung_Da.mp3",
        "Pehla_Nasha.mp3",
        "Tu_Jaane_Na.mp3"
    ]  

    current_index = 0
    play_music(playlist[current_index])

    while True:
        command = input("Enter 'pause', 'unpause', 'stop', 'next', or 'exit' to quit: ")
        
        if command == "pause":
            pause_music()
        elif command == "unpause":
            unpause_music()
        elif command == "next":
            current_index = play_next_song(playlist, current_index)
        elif command == "exit":
            stop_music()
            break
        else:
            print("Invalid command. Try again.")
