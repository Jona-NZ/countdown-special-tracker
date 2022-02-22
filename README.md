# Countdown Special Tracker

A python script that emails the user if an item at Countdown is on special.

<img src="https://i.imgur.com/tzlDfQZ.png" width="400">

### Usage

How you wish to utilise the script is up to you; either host it on a server and run it on a schedule, or incorporate it into a web app.

### Requirements

1. Ensure you have a `.env` file in the root directory prior to running the script:
```
EMAIL_USER = login_email_for_sending_account
EMAIL_PASS = login_password_for_sending_account
TO_EMAIL = receiving_email_address
```

2. Download and install the relevant chromedriver.exe and place it into the root folder.

3. Update the SMTP information in the ```email()``` method. If using Gmail, you must grant less secure apps access to your account under your Google account settings.


## Authors

* Jona Stevenson - [GitHub](https://github.com/Jona-NZ) - [LinkedIn](https://www.linkedin.com/in/jona-stevenson-nz/)
