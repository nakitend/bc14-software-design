# Define the MusicPlayer class
class MusicPlayer:
    def play(self, song: str):
        print(f"Playing {song}")

    def stop(self):
        print("Music stopped")

# Define the Laptop class
class Laptop:
    def power_on(self):
        print("Laptop is powering on.")

    def power_off(self):
        print("Laptop is powering off.")

    def connect_to_wifi(self):
        print("Connecting to Wi-Fi.")
        return True

    def connect_to_bluetooth(self):
        print("Connecting to Bluetooth.")
        return True

    def fold(self):
        print("Folding...")

class ComputerFacade:
    def __init__(self, laptop: Laptop, music_player: MusicPlayer):
        self.laptop = laptop
        self.music_player = music_player

    def turn_on(self):
        # Power up the computer components
        self.laptop.power_on()

    def turn_off(self):
        # Power down the computer components
        self.laptop.power_off()

    def connect_to_wifi(self):
        # Connect to Wi-Fi using the laptop's Wi-Fi capability
        self.laptop.connect_to_wifi()

    def connect_to_bluetooth(self):
        # Connect to Bluetooth using the laptop's Bluetooth capability
        self.laptop.connect_to_bluetooth()

    def fold(self):
        # Fold the laptop
        self.laptop.fold()

    def play_music(self, song: str):
        # Play a song using the music player
        self.music_player.play(song)

    def stop_music(self):
        # Stop the music player
        self.music_player.stop()

# Now, you can use the ComputerFacade to interact with the laptop's components and the music player
laptop = Laptop()
music_player = MusicPlayer()
computer_facade = ComputerFacade(laptop, music_player)

# Power on the computer
computer_facade.turn_on()

# Connect to Wi-Fi
computer_facade.connect_to_wifi()

# Connect to Bluetooth
computer_facade.connect_to_bluetooth()

# Fold the laptop
computer_facade.fold()

# Play music
computer_facade.play_music("Favorite Song")

# Stop the music
computer_facade.stop_music()

# Power off the computer
computer_facade.turn_off()
