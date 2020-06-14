# airflow-email-bot
Automatically send email using AIrflow

Used https://github.com/happilyeverafter95/slack-airflow to send automated emails to my friends

## How to setup your App password
1. Go to your google account (press the circle icon at top right)
2. Choose security
3. If not already done set up 2-Step Vertification
4. On the "Signing to Google" panel, choose App Passwords
5. Select the app and device type you are using
6. Generate a code by pressing Generate
7. change these fields in airflow.cfg (confugration file)

```
# smtp server here
smtp_host = smtp.gmail.com
smtp_starttls = True
smtp_ssl = False
# Uncomment and set the user/pass settings if you want to use SMTP AUTH
smtp_user = YOUR EMAIL
smtp_password = YOUR 16 DIGIT APP CODE
smtp_port = 587
smtp_mail_from = YOUR EMAIL AGAIN
```
