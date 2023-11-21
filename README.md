# Health AI-Powered Symptom and Diagnosis Guidance

## Overview

This application aims to provide users with preliminary medical advice by allowing them to describe their symptoms through an AI-powered chatbot interface. It assists users in deciding whether they need immediate in-person medical care based on the provided advice.

### Key Features

- User account creation and authentication.
- Symptom description through a conversational chatbot.
- Preliminary diagnosis or medical advice based on symptoms.
- User interaction history tracking.
- Continuous improvement through user feedback and model updates.

## Technology Stack

- **Backend**: Python Django, Django REST Framework
- **Database**: MySQL
- **Authentication**: JWT for securing API endpoints
- **Data Science Model**: Python with scikit-learn, TensorFlow, or PyTorch

## Project Structure

- `health_ai_backend/`: Root directory of the Django project.
    - `app/`: Directory containing Django applications/modules.
        - `authentication/`: Handles user authentication-related functionalities.
        - `symptoms/`: Manages symptom input functionalities.
        - `diagnosis/`: Manages diagnostic result functionalities.
        - `history/`: Manages user interaction history functionalities.
        - `feedback/`: Deals with user feedback functionalities.
        - `model_update/`: Manages model update log functionalities.
    - `health_ai_backend/`: Django project settings and configurations.
    - `manage.py`: Django project management script.
    - `requirements.txt`: File containing all the required Python dependencies.

## API Endpoints

Detailed API documentation available in the [API_ENDPOINTS.md](API_ENDPOINTS.md) file.

## Database Schema

The database schema for the application is detailed in the [DATABASE_SCHEMA.md](DATABASE_SCHEMA.md) file.

## Getting Started

1. Clone the repository: `git clone <repository_url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure the database settings in `health_ai_backend/settings.py`
4. Run migrations: `python manage.py migrate`
5. Start the Django server: `python manage.py runserver`

## Usage

- Access the API endpoints through the specified routes.
- Implement frontend interfaces to interact with the backend services.

## Contributors

- **[Abakpa Dominic]**: [GitHub Profile](https://github.com/DT-GAMER)
- **[Ezeali Daniel]**: [GitHub Profile](https://github.com/eodaneze)
- **[Odinaka Emmanuel]**: [GitHub Profile](https://github.com/Emmanuel-Odinaka)
-  **[Glory Aderinwale]**: [GitHub Profile](https://github.com/GloryOyinkansola)
-   **[Muyiwa Akinyemi]**: [GitHub Profile](https://github.com/TheUnusualD)

## License

This project is licensed under the [MIT License](LICENSE).
