from gerby.application import app
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv('.flaskenv')
    app.run()