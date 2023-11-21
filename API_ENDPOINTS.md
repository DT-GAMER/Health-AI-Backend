# Health AI API Endpoints

This document provides an overview of the API endpoints available for the Health AI-Powered Symptom and Diagnosis Guidance application.

## Authentication Endpoints

### User Registration

- **Endpoint:** `POST /api/auth/register`
- **Description:** Create a new user account.
- **Request Body:**
  - `username` (string): User's username
  - `email` (string): User's email address
  - `password` (string): User's password
- **Response:**
  - `message` (string): Success message or error details

### User Login

- **Endpoint:** `POST /api/auth/login`
- **Description:** User login to access personalized features.
- **Request Body:**
  - `email` (string): User's email address
  - `password` (string): User's password
- **Response:**
  - `token` (string): JWT token for authenticated access
  - `user_id` (string): User's unique identifier
  - `username` (string): User's username

## Symptom Input and Diagnosis Endpoints

### Submit Symptoms

- **Endpoint:** `POST /api/symptoms`
- **Description:** Submit user's symptoms for diagnosis.
- **Request Body:**
  - `symptoms` (string): Description of user's symptoms
  - `user_id` (string): User's unique identifier
- **Response:**
  - `diagnosis` (string): Preliminary diagnosis or medical advice

## User Interaction History Endpoints

### Retrieve History

- **Endpoint:** `GET /api/history`
- **Description:** Retrieve user interaction history.
- **Request Parameters:**
  - `user_id` (string): User's unique identifier
  - `time_period` (string): Time parameter for history retrieval (e.g., today, past 7 days, 30 days)
- **Response:**
  - `history` (array of objects): Array containing interaction history (symptoms, diagnoses, timestamps)

## Continuous Improvement Endpoints

### Submit Feedback

- **Endpoint:** `POST /api/feedback`
- **Description:** Submit user feedback for diagnostic advice.
- **Request Body:**
  - `user_id` (string): User's unique identifier
  - `feedback` (string): User's feedback or ratings
- **Response:**
  - `message` (string): Success message confirming feedback submission

### Trigger Model Update

- **Endpoint:** `POST /api/model/update`
- **Description:** Trigger model update/retraining process.
- **Request Body:**
  - `trigger_key` (string): Key to trigger model update (e.g., admin access key)
- **Response:**
  - `message` (string): Success message or error details for model update trigger
