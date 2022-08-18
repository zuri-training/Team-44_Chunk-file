"""Application entry point."""
from split_app import create_app
import os

app = create_app()

if __name__ == "__main__":
    app.run()
