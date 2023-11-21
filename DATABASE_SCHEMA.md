# Health AI Database Schema

This document outlines the database schema design for the Health AI-Powered Symptom and Diagnosis Guidance application.

## User Table

- **`user_id`** (Primary Key): Unique identifier for the user
- **`username`**: User's username
- **`email`**: User's email address
- **`password`**: Hashed password for user authentication

## Symptom Input Table

- **`symptom_id`** (Primary Key): Unique identifier for each symptom input
- **`user_id`** (Foreign Key): Corresponding user ID for the symptom input
- **`symptoms`**: Description of user's symptoms
- **`timestamp`**: Timestamp for the symptom input

## Diagnostic Result Table

- **`result_id`** (Primary Key): Unique identifier for each diagnostic result
- **`user_id`** (Foreign Key): Corresponding user ID for the diagnostic result
- **`symptom_id`** (Foreign Key): Corresponding symptom ID linked to the diagnosis
- **`diagnosis`**: Preliminary diagnosis or medical advice
- **`timestamp`**: Timestamp for the diagnostic result

## Interaction History Table

- **`interaction_id`** (Primary Key): Unique identifier for each interaction history entry
- **`user_id`** (Foreign Key): Corresponding user ID for the interaction history
- **`symptom_id`** (Foreign Key): Corresponding symptom ID linked to the interaction
- **`diagnosis_id`** (Foreign Key): Corresponding diagnosis ID linked to the interaction
- **`timestamp`**: Timestamp for the interaction

## Feedback Table

- **`feedback_id`** (Primary Key): Unique identifier for each feedback entry
- **`user_id`** (Foreign Key): Corresponding user ID for the feedback
- **`feedback_content`**: User's feedback or ratings
- **`timestamp`**: Timestamp for the feedback submission

## Model Update Log Table

- **`update_id`** (Primary Key): Unique identifier for each model update log entry
- **`trigger_key`**: Key used to trigger the model update
- **`timestamp`**: Timestamp for the model update trigger
