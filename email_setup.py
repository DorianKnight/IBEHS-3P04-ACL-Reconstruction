
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Setup port number and server name

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

# Set up the email lists
email_from = "rebalancecanada@gmail.com"
email_list = ["nehetea@mcmaster.ca"]

# Define the password (better to reference externally)
# As shown in the video this password is now dead, left in as example only
pswd = 'nylbirmhjajcnciy'


file_names = ['sebt/Anterolateral_SEBT_KneeAngles.png', 'sebt/Anteromedial_SEBT_KneeAngles.png',
              'sebt/Anterior_SEBT_KneeAngles.png', 'sebt/Lateral_SEBT_KneeAngles.png', 'sebt/Medial_SEBT_KneeAngles',
              'sebt/Posterolateral_SEBT_KneeAngles', 'sebt/Posteromedial_SEBT_KneeAngles', 'sebt/Posterior_SEBT_KneeAngles',
              'CofM_images/Anterolateral_SEBT_CofM.png', 'CofM_images/Anteromedial_SEBT_CofM.png',
              'CofM_images/Anterior_SEBT_CofM.png', 'CofM_images/Lateral_SEBT_CofM.png',
              'CofM_images/Medial_SEBT_CofM.png', 'CofM_images/Posterolateral_SEBT_CofM.png',
              'CofM_images/Posteromedial_SEBT_CofM.png', 'CofM_images/Posterior_SEBT_CofM.png']

anterior_SEBT = []
anterolateral_SEBT = []
anteromedial_SEBT = []
lateral_SEBT = []
medial_SEBT = []
posterolateral_SEBT = []
posteromedial_SEBT = []
posterior_SEBT = []


# Define the email function (dont call it email!)


def send_emails(email_list, file_names, scores):
    # name the email subject
    subject = "ACL Rehab data for Patient Doe, John"

    # add processing for scores

    for person in email_list:

        # Make the body of the email
        body = f"""
        Dear Clinician, 
        blah blah blah blah
        """
        # make a MIME object to define parts of the email
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        # Attach the body of the message
        msg.attach(MIMEText(body, 'plain'))

        for filename in file_names:

            try:
                # Open the file in python as a binary
                # r for read and b for binary
                attachment = open(filename, 'rb')
            except FileNotFoundError:
                continue

            # Encode as base 64
            attachment_package = MIMEBase('application', 'octet-stream')
            attachment_package.set_payload((attachment).read())
            encoders.encode_base64(attachment_package)
            attachment_package.add_header(
                'Content-Disposition', "attachment; filename= " + filename)
            msg.attach(attachment_package)

        # Cast as string
        text = msg.as_string()

        # Connect with the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()

        # Send emails to "person" as list is iterated
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent to: {person}")
        print()

    # Close the port
    TIE_server.quit()


# Run the function
#send_emails(email_list, file_names, [])
