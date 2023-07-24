Baigiamasis darbas


Description
TrustyTails is a web application that provides pet services, allowing users to reserve time for their pets and choose from various pet services. Users can create an account, view available services, and make reservations for their pets.

Table of Contents
Installation
Usage
Features
Technologies
Contributing

Installation
To run TrustyTails on your local machine, follow these steps:

Clone the repository:
$ git clone <repository_url>
$ cd trustytails

Install the required dependencies:
$ pip install -r requirements.txt

Apply database migrations:
$ python manage.py migrate

Run the development server:
$ python manage.py runserver

You can access the application in your web browser at http://127.0.0.1:8000/.

Usage

Sign Up: Create a new account to access the full functionality of the application.
Log In: Existing users can log in with their credentials.
Profile: Shows reservation information.
Services: Browse the available pet services provided by TrustyTails.
Reserve Time: Make a reservation for your pet by selecting the date, time, and desired services.
Reservation Success: After making a reservation, receive a confirmation email with the reservation details.

Features
User Authentication: Allow users to sign up and log in to access the application.
Pet Services: Display a list of available pet services for users to choose from.
Reservation: Allow users to make reservations for their pets, selecting the date, time, and services.
Email Confirmation: Send a confirmation email to users after making a reservation.

Technologies
Django: Web framework used for building the application.
Django Rest Framework: For creating RESTful APIs.
SQLlite: A database management system for storing data.
HTML, CSS, JAVASCRIPT: Frontend technologies for the user interface.
Decouple: For managing environment variables.

