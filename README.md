# Teach Me App

Teach Me App is a flashcard application designed to help users create, manage, and train with flashcards. The application allows users to upload documents, generate flashcards, and train on specific boxes of cards.

## Features

- Create new flashcards
- Upload documents to generate flashcards
- Train on specific boxes of cards
- Track known and unknown cards
- Delete entire boxes of cards

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- A virtual environment tool (e.g., `venv` or `virtualenv`)

### Steps

1. **Clone the repository:**
   ```
   git clone https://github.com/pr0fi7/teach_me_app.git
   cd teach_me_app
   ```
2. **Create and activate a virtual environment:**
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```
4. **Run database migrations:**
   ```
   python manage.py migrate
   ```
5. **Start the development server:**
   ```
   python manage.py runserver
   ```
6. **Access the application:**

   Open your browser and go to ```http://127.0.0.1:8000/```

## Usage

### Creating Flashcards

1. Navigate to the "All Cards" page.
2. Click on "✨ Create New Card".
3. Fill out the form with the question and answer, and select the box number.
4. Click "Save" to create the flashcard.

### Uploading Documents

1. Navigate to the "All Cards" page.
2. Click on "Upload a document".
3. Choose a file and set the slider value.
4. Click "Upload" to generate flashcards from the document.

### Training with Flashcards

1. Navigate to the "All Cards" page.
2. Click on "Train Cards".
3. Select a box to train with.
4. Answer each flashcard by indicating whether you knew the answer or not.
5. Continue training until all cards in the box are reviewed.

### Managing Boxes

1. Navigate to the "All Cards" page.
2. Each box of cards will have a "🗑 Delete Box" button.
3. Click the delete button to remove all cards in the box.

## Project Structure

- `cards/` - Contains the main application code, including models, views, forms, and templates.
- `templates/` - Contains HTML templates for rendering the application pages.
- `static/` - Contains static files (CSS, JavaScript, images).
- `manage.py` - Django's command-line utility for administrative tasks.
- `requirements.txt` - Lists the dependencies required to run the project.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue on GitHub.




