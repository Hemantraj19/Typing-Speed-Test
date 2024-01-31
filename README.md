# Typing Speed Test

This simple typing speed test is built using Python and Tkinter. Users can test their typing speed and accuracy by typing the displayed text within a set time limit.

## Prerequisites

- Python 3.x
- Tkinter library
- `requests` library (install using `pip install requests`)

## Usage

1. Clone the repository.

    ```bash
    git clone https://github.com/your-username/typing-speed-test.git
    ```

2. Navigate to the project directory.

    ```bash
    cd typing-speed-test
    ```

3. Run the `main.py` script.

    ```bash
    python main.py
    ```

4. Type the displayed text as fast and accurately as possible within the time limit.

## Features

- Displays a random set of 200 words for the user to type, fetches the words using API.
- Timer starts when the user begins typing.
- Calculates typing speed in words per minute (WPM) and accuracy.
- Supports backspace to correct mistakes.
- Provides a restart button to reset the game.

## File Structure

- `main.py`: Main script to run the typing speed test game.
- `get_words.py`: Module to fetch random words from an API.
- `ui.py`: Module containing the user interface (UI) elements.

## API Key

Replace `"your api key"` in `get_words.py` with your actual API key for fetching random words.

## Customization

Feel free to customize the code or UI elements to suit your preferences.

## Acknowledgments

- The project uses the [api-ninjas](https://api.api-ninjas.com/) API to fetch random words.
