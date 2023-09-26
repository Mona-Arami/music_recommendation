# Music Recommendation ML App

Welcome to the masterMind Music Recommendation ML App! This application leverages machine learning to provide personalized music recommendations based on user preferences. Whether you're a music enthusiast or just looking for some new tunes, this app is designed to help you discover your next favorite songs.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Dataset](#dataset)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How it Works](#how-it-works)

## Features

- **Personalized Recommendations:** Our machine learning algorithms analyze your preferences to suggest music tailored just for you.

- **Explore New Music:** Discover new genres, and songs that match your taste but may not be on your radar yet.

- **User-Friendly Interface:** An intuitive and user-friendly interface makes it easy to navigate and find the music you love.

- **Cross-Platform:** Access your music recommendations from any device with our web and mobile app support.

## Getting Started

wW will build this recommendation engine with Streamlit, the k-Nearest Neighbors machine learning model with Scikit-learn, and deploy our website using AWS EC2.

## Dataset

Before we start building our application, we need a music dataset. For our dataset, we will use the Spotify and Genius Track Dataset from Kaggle. This dataset contains information on thousands of albums, artists, and songs that are collected from the Spotify platform using its API. In addition, the dataset also contains lower-level audio features of the songs, as well as their lyrics.

### Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- Python 3.x
- Virtualenv (optional but recommended)
- streamlit

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Mona-Arami/music_recommendation.git
   ```

2. Change into the project directory:

   ```bash
   cd music-recommendation
   ```

3. (Optional) Create a virtual environment to isolate dependencies:

   ```bash
   virtualenv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the application:

   ```bash
   streamlit run app.py
   ```
## How it Works

The app should now be running locally on [http://localhost:8501/](http://localhost:8501/). You can access it in your web browser.
Also Music Recommendation ML App on AWS EC2 instance, you can access to it [http://3.128.95.93:8501/](http://3.128.95.93:8501/).