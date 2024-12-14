from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)

        # Background image (bubbles.png as wallpaper)
        bg = AsyncImage(source='bubbles.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(bg)

        # Using FloatLayout for flexibility in positioning
        layout = FloatLayout()
        self.add_widget(layout)

        # Stylish Donate button
        donate_button = Button(
            text="start",
            font_size="20sp",
            background_color=(0.2, 0.5, 0.8, 1),  # Deep blue color
            color=(1, 1, 1, 1),  # White text color
            size_hint=(None, None),
            size=(200, 60),
            pos_hint={'center_x': 0.5, 'center_y': 0.2}
        )
        donate_button.bind(on_press=self.go_to_second_screen)
        layout.add_widget(donate_button)

    def go_to_second_screen(self, instance):
        self.manager.current = 'second'


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)

        # Background image (purple.png as wallpaper)
        bg = AsyncImage(source='purple.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(bg)

        # Using FloatLayout for flexibility in positioning
        layout = FloatLayout()
        self.add_widget(layout)

        # Additional widgets or buttons for the SecondScreen can be added here


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))

        self.icon = 'icon.ico'  # Your app icon
        return sm
