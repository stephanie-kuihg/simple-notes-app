# able to import entire folder of python packages & functions
from website import create_app

app = create_app()

if __name__ == '__main__':       # important to ensure that it runs the correct python package
    app.run(debug=True)
    # auto update app with changes in code
    # typically set to True in devt, not production
