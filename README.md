# Health & Disease Chatbot

Health & Disease Chatbot is an AI-powered conversational assistant designed to provide health-related advice, dietary tips, and answers to common queries about diabetes and general well-being. This project leverages the ChatterBot library for natural language processing and Flask for building the web interface.

---

## Features

- **Health-Centric Conversations**: Pretrained on health-related datasets to answer questions about diabetes management, prevention, and general symptoms.
- **Interactive UI**: User-friendly web interface built with HTML, CSS, and JavaScript.
- **Customizable**: Expandable dataset to include more health topics or customize chatbot behavior.
- **Real-Time Interaction**: Powered by Flask for seamless query handling.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Technical Details](#technical-details)
4. [Dataset and Training](#dataset-and-training)
5. [Architecture Overview](#architecture-overview)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/health-chatbot.git
   cd health-chatbot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```
---

## Usage

### Web Interface

- Open the chatbot interface in your browser.
- Type your health-related query (e.g., "What should I avoid if I have diabetes?").
- Receive informative and concise responses from the chatbot.

### Command-Line Interface

Run the `main.py` script for a CLI experience:
```bash
python main.py
```

---

## Technical Details

### Key Components
- **Flask**: Backend framework for web interface.
- **ChatterBot**: Library for conversational AI.
- **HTML/CSS/JS**: Frontend technologies for an interactive interface.

### File Structure
```
/health-chatbot
├── app.py               # Flask app entry point
├── chatbot_logic.py     # Core chatbot logic and training
├── data/
│   └── health_data.py   # Dataset for chatbot
├── requirements.txt     # Required dependencies
├── static/
│   └── style.css        # Styling for web UI
└── templates/
    └── index.html       # Frontend HTML template
```

---

## Dataset and Training

The chatbot is trained on a dataset of curated health conversations about diabetes and general health topics. It uses ChatterBot's `ListTrainer` to build responses tailored to the dataset.

---

## Architecture Overview

```mermaid
graph TD
    A[User Input] -->|HTTP Request| B[Flask Backend]
    B --> C[Chatbot Logic]
    C --> D[ChatterBot Response]
    D -->|HTTP Response| E[Web Interface]
```

---
