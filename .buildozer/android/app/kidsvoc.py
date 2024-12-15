from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from gtts import gTTS
import pygame
import os


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)

        # Background image
        bg = AsyncImage(source='bubbles.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(bg)

        layout = FloatLayout()
        self.add_widget(layout)

        start_button = Button(
            text="Start",
            font_size="20sp",
            background_color=(0.2, 0.5, 0.8, 1),
            color=(1, 1, 1, 1),
            size_hint=(None, None),
            size=(200, 60),
            pos_hint={'center_x': 0.5, 'center_y': 0.2}
        )
        start_button.bind(on_press=self.go_to_second_screen)
        layout.add_widget(start_button)

    def go_to_second_screen(self, instance):
        self.manager.current = 'second'


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)

        # Background image
        bg = AsyncImage(source='purple.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(bg)

        layout = FloatLayout()
        self.add_widget(layout)

        grid = GridLayout(
            cols=2,
            spacing=20,
            padding=[20, 50, 20, 50],
            size_hint=(None, None),
            size=(320, 400),
            pos_hint={'center_x': 0.45, 'center_y': 0.5}
        )
        layout.add_widget(grid)

        categories = ["Animals", "Colors", "Fruits", "Numbers", "Shapes", "Actions"]

        for category in categories:
            button = Button(
                text=category,
                font_size="18sp",
                background_color=(0.2, 0.5, 0.8, 1),
                color=(1, 1, 1, 1),
                size_hint=(None, None),
                size=(150, 80)
            )
            button.bind(on_press=self.on_category_selected)
            grid.add_widget(button)

    def on_category_selected(self, instance):
        if instance.text == "Animals":
            self.manager.current = 'animals'



class AnimalScreen(Screen):
    def __init__(self, **kwargs):
        super(AnimalScreen, self).__init__(**kwargs)

        # Initialize pygame mixer
        pygame.mixer.init()

        # Background image (galaxy.png)
        bg = AsyncImage(source='galaxy.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(bg)

        # Main layout: Vertical Box for all animal cards
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=[10, 10, 10, 10], size_hint=(1, None))
        main_layout.bind(minimum_height=main_layout.setter('height'))  # Dynamically adjust height

        # Scroll view to enable scrolling if needed
        scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False, do_scroll_y=True)
        scroll_view.add_widget(main_layout)
        self.add_widget(scroll_view)

        # Animal data
        animals = [
            {"name_ar": "أسد", "name_fr": "Lion", "image": "lion.png", "audio_ar": "lion_ar.mp3", "audio_fr": "lion_fr.mp3"},
            {"name_ar": "فيل", "name_fr": "Éléphant", "image": "elephant.png", "audio_ar": "elephant_ar.mp3", "audio_fr": "elephant_fr.mp3"},
            {"name_ar": "قرد", "name_fr": "Singe", "image": "monkey.png", "audio_ar": "monkey_ar.mp3", "audio_fr": "monkey_fr.mp3"},
            {"name_ar": "نمر", "name_fr": "Tigre", "image": "tiger.png", "audio_ar": "tiger_ar.mp3", "audio_fr": "tiger_fr.mp3"}
        ]

        # Add a card for each animal
        for animal in animals:
            # Layout for each animal row
            row_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=90, spacing=5)

            # Image of the animal
            img = AsyncImage(source=animal['image'], size_hint=(None, None), size=(70, 70))
            row_layout.add_widget(img)

            # Audio buttons
            button_layout = BoxLayout(orientation='vertical', size_hint=(None, None), spacing=2, width=60)
            audio_ar_button = Button(text="🔊 AR", size_hint=(None, None), size=(50, 25))
            audio_ar_button.bind(on_press=lambda x, audio=animal["audio_ar"]: self.play_audio(audio))
            audio_fr_button = Button(text="🔊 FR", size_hint=(None, None), size=(50, 25))
            audio_fr_button.bind(on_press=lambda x, audio=animal["audio_fr"]: self.play_audio(audio))
            button_layout.add_widget(audio_ar_button)
            button_layout.add_widget(audio_fr_button)
            row_layout.add_widget(button_layout)

            # Add the row layout to the main layout
            main_layout.add_widget(row_layout)

    def play_audio(self, audio_file):
        try:
            if not os.path.exists(audio_file):
                print(f"Audio file not found: {audio_file}")
                return

            # Stop any ongoing audio
            pygame.mixer.music.stop()

            # Load and play the audio file
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()

            # Wait until the audio finishes playing
            while pygame.mixer.music.get_busy():
                continue

        except Exception as e:
            print(f"Error playing audio: {e}")




class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(AnimalScreen(name='animals'))

        self.icon = 'icon.ico'
        return sm


if __name__ == '__main__':
    MyApp().run()
