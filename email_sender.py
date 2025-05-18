import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

# Sender's email credentials
sender_email = "pes2ug22cs901@gmail.com"
app_password = "eofeqjxfzizpzsqu"

# Recipient's email
recipient_email = "rajumm1996@gmail.com"

# Function to send an email alert
def alert_sender(data_frame):
    try:
        # Convert DataFrame to an HTML table
        body = data_frame.to_html(index=False, border=1)

        # Custom message to add before or after the table
        custom_message = """
        <p><strong>Important Alert:</strong></p>
        <p>The patient's condition is very critical. Please react immediately and reach the location provided below.</p>
        <p>Contact the supported mobile number for more details.</p>
        <p><strong>Thank you for your prompt attention!</strong></p>
        <p><hr></p>
        """

        # Combine the message with the HTML table
        full_body = custom_message + body

        # Create the multipart message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = "Health Condition Alert"

        # Attach the combined body to the email
        message.attach(MIMEText(full_body, "html"))

        # Connect to the Gmail SMTP server using SSL
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            # Login to the sender email account
            server.login(sender_email, app_password)

            # Send the email
            server.sendmail(sender_email, recipient_email, message.as_string())

        print("Email sent successfully to", recipient_email)
    except Exception as e:
        print(f"Failed to send email: {e}")