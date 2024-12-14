# main.py
from kivy.config import Config

# Set the size to a common Android phone screen size
Config.set('graphics', 'width', '360')  # Width for mobile devices
Config.set('graphics', 'height', '640')  # Height for mobile devices
Config.write()

from kidsvoc import MyApp  # Importing the MyApp class from the fund_app module

def main():
    # Create an instance of the MyApp class and start the application
    app = MyApp()
    app.run()

if __name__ == '__main__':
    main()
