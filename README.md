# Python Course - Ruben Ocasio
# Legendary Developers in the making.
Welcome to Python Cohort - December 2023, where we dive into the exciting world of web development with Python and Flask! This repository contains all the demo code and lectures for the course. Follow the instructions below to get started.

## Installation

Before you begin, make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

1. **Clone the Repository**:  
   `git clone https://github.com/[YourGitHubUsername]/[YourRepoName].git`
2. **Navigate to the Directory**:  
   `cd [YourRepoName]`
3. **Create a Virtual Environment** (Optional but recommended):  
   `python -m venv venv`
4. **Activate the Virtual Environment**:  
   - Windows: `venv\Scripts\activate`
   - MacOS/Linux: `source venv/bin/activate`
5. **Install Flask**:  
   `pip install Flask`

## Setting Up a Basic Flask Project

1. **Create a new Python file** (e.g., `app.py`).
2. **Import Flask** and create an instance of the Flask class:
   ```python
   from flask import Flask
   app = Flask(__name__)
   ```
3. **Define routes** using decorators:
   ```python
   @app.route('/')
   def home():
       return 'Hello, Flask!'
   ```
4. **Run the app**:
   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```

## Tips for Success

- **Understand the Basics**: Make sure you're comfortable with basic Python syntax.
- **Follow Along**: Try coding along with the demos and lectures.
- **Practice**: The best way to learn is by doing. Try creating your own small projects using Flask.
- **Ask Questions**: If you're stuck, don't hesitate to ask for help.
- **Read the Flask Documentation**: The [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/) is a great resource.

## Contact

For any queries regarding the course, feel free to reach out:  
Email: [Your Email]  
LinkedIn: [Your LinkedIn Profile]

---

Feel free to modify and expand this template based on your course content and style. Good luck with your teaching!
