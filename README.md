\# AI Study Assistant



An AI-powered study assistant built with Flask, SQLite, and Ollama.



The application allows students to create an account, save their study notes, view their notes, and ask questions based on their saved notes using a locally running AI model.



\## Features



\- User registration and login

\- Secure password hashing

\- Session-based authentication

\- Save and view study notes

\- Ask questions about saved notes

\- AI-generated answers using Ollama

\- SQLite database for storing users and notes

\- Simple web interface using HTML and CSS



\## Technologies Used



\- Python

\- Flask

\- SQLite

\- Ollama

\- HTML

\- CSS



\## AI Model



This project uses Ollama to run the phi3 language model locally.



The AI processes the student's saved notes along with their question and generates a study-focused response.



\## Project Structure



ai-study-assistant/

│

├── app.py

├── database.py

├── requirements.txt

├── .gitignore

│

├── static/

│   └── style.css

│

└── templates/

&#x20;   ├── ask.html

&#x20;   ├── dashboard.html

&#x20;   ├── home.html

&#x20;   ├── login.html

&#x20;   ├── notes.html

&#x20;   ├── register.html

&#x20;   ├── upload.html

&#x20;   └── users.html



\## Installation



\### 1. Clone the repository



git clone https://github.com/mohammadibrahimata/ai-study-assistant.git

cd ai-study-assistant



\### 2. Install Python dependencies



pip install -r requirements.txt



\### 3. Install Ollama



Install Ollama on your computer and make sure the phi3 model is available:



ollama pull phi3



\### 4. Create the database



python database.py



\### 5. Run the Flask application



python app.py



The application will run locally at:



http://127.0.0.1:5000



\## How It Works



1\. A user registers an account.

2\. The password is securely hashed before being stored.

3\. The user logs in and accesses the dashboard.

4\. The user can save study notes.

5\. The notes are stored in SQLite.

6\. When the user asks a question, the application retrieves the saved notes.

7\. The notes and question are sent to the local Ollama model.

8\. The AI generates an answer based on the study material.



\## Purpose



This project was built as a learning project to practice:



\- Python

\- Flask web development

\- SQLite databases

\- User authentication

\- Local AI models

\- Connecting a web application to an AI system

\- Git and GitHub



\## Author



Mohammad Ibrahim Ata



B.Tech Information Technology Student

