# main.py
from fund_app import MyApp  # Importing the MyApp class from the fundr_app module

def main():
    # Create an instance of the MyApp class and start the application
    app = MyApp()
    app.run()

# This ensures that the main function is only called when the script is executed directly, not when it's imported
if __name__ == '__main__':
    main()