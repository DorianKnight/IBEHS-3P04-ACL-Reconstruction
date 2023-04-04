
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
from processing_funcs import *

# Setup port number and server name

smtp_port = 587          # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

# Set up the email lists
email_from = "rebalancecanada@gmail.com"
email_list = ["nehetea@mcmaster.ca"]

# Define the password (better to reference externally)
# As shown in the video this password is now dead, left in as example only
pswd = 'ziakhqieazvadhox'

test_SEBT_data = {
    'Anterior': [[1, 150, 1], [2, 130, 1]],
    'Anterolateral': [[1, 150, 1], [2, 130, 1]],
    'Anteromedial': [[1, 150, 1], [2, 130, 1]],
    'Lateral': [[1, 150, 1], [2, 130, 1]],
    'Medial': [[1, 150, 1], [2, 130, 1]],
    'Posterolateral': [[1, 150, 1], [2, 130, 1]],
    'Posteromedial': [[1, 150, 1], [2, 130, 1]],
    'Posterior': [[1, 150, 1], [2, 130, 1]]
}


# ONLY FOR TESTING // DELETE LATER
a = [(1.6209302325581396, -1.4965116279069766), (1.4548387096774191, -
                                                 1.5096774193548386), (1.5043165467625896, -1.0521582733812949), (1.3666666666666665, -1.6316326530612246),
     (1.1832214765100668, -2.080872483221476), (0.8424657534246573, -1.1219178082191779), (0.7653333333333333, -
                                                                                           0.7799999999999998), (1.010958904109589, -0.8013698630136988), (1.1549295774647887, -0.32957746478873207),
     (1.4033557046979863, 0.43187919463087227), (1.6785234899328856, 0.03926174496644311), (
    1.7335570469798656, -0.35335570469798644), (1.589795918367347, 0.0397959183673471),
    (1.544155844155844, 0.4558441558441558), (1.1714285714285713, -0.4558441558441558), (0.43617021276595747, -1.8670212765957446), (0.43617021276595747, 0.7053191489361701), (0.6594405594405592, 1.104545454545455), (1.5476821192052979, 0.11622516556291398), (1.5769230769230764, -0.6954545454545458), (1.5375, -0.07312499999999993), (0.9595744680851063, 0.2074468085106383), (1.384415584415584, 0.9876623376623378), (1.6746478873239437,
                                                                                                                                                                                                                                                                                                                                                                                                                                  0.9063380281690144), (1.7038961038961038, 1.1396103896103893), (1.7105960264900664, -0.6586092715231787), (1.5228571428571427, 0.0835714285714289), (1.6346405228758167, -0.19117647058823528), (1.6506493506493505, -0.07597402597402664), (1.2356164383561643, -0.4808219178082195), (0.8519480519480519, -0.8357142857142859), (0.7202702702702702, -0.7114864864864862), (0.5228187919463088, -0.03926174496644311), (0.8960264900662253, -0.19370860927152317), (1.0819444444444444, -0.5687499999999999), (1.03943661971831, 0.4119718309859155), (1.3289655172413792, 0.36310344827586233), (1.2551020408163265, 1.3132653061224493), (1.1232876712328765, 2.8047945205479454), (1.3479452054794518, 2.484246575342466), (1.5853333333333333, 1.1700000000000004), (1.4933774834437084, 1.5884105960264894), (1.5340136054421767, 2.029591836734694), (1.4436619718309855, 2.8838028169014076), (1.4213333333333331, 2.262), (0.6648648648648647, 0.5533783783783786), (0.5447552447552448, -0.8590909090909089), (0.8613445378151258, -1.4256302521008402), (1.198461538461538, -1.35), (1.5374999999999996, 0.7312500000000002), (1.3666666666666667, 1.95), (1.9421052631578943, 2.155263157894737), (1.7571428571428567, 3.6214285714285706), (1.3666666666666667, 3.6214285714285706), (1.64, 1.7549999999999994), (1.9421052631578943, 0.9236842105263157), (1.9421052631578943, 0.9236842105263157), (1.6882352941176468, 1.032352941176471), (1.9421052631578943, 0.9236842105263157), (1.822222222222222, 1.2999999999999998), (2.2777777777777772, 1.2999999999999998), (2.3736842105263154, 1.5394736842105259), (2.170588235294117, 1.0323529411764705), (2.1705882352941175, 0.34411764705882364), (2.05, 0.0), (1.9133333333333333, 1.1700000000000004), (1.1181818181818182, 1.5954545454545452), (-1.3666666666666665, 5.849999999999999), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
b = [(1.40335, 0.43187), (1.678523, 0.03926), (1.73355, -0.3533)]

test_CofM_data = {
    'Anterior': [a, b],
    'Anterolateral': [a, b],
    'Anteromedial': [a, b],
    'Lateral': [a, b],
    'Medial': [a, b],
    'Posterolateral': [a, b],
    'Posteromedial': [a, b],
    'Posterior': [a, b]
}
# ONLY FOR TESTING ABOVE DELETE LATER!!!


# Define the email function (dont call it email!)
def send_emails(email_list, file_names, SEBT_data, CofM_data):
    # deviations = get_CofM_deviations(CofM_data)

    stability_score_CofM, std_x_diff, std_y_diff = get_CofM_deviations(
        CofM_data)
    stability_score_angles, diffs = get_knee_angle_scores(SEBT_data)

    SEBT_data_string_x = '\n'
    for item in std_x_diff:
        SEBT_data_string_x += f'{item}: {std_x_diff[item]} cm\n'
    SEBT_data_string_y = '\n'
    for item in std_y_diff:
        SEBT_data_string_y += f'{item}: {std_y_diff[item]} cm\n'
    SEBT_angle_diffs = '\n'
    for item in diffs:
        SEBT_angle_diffs += f'{item}: {diffs[item]}° \n'

    # name the email subject
    subject = "ACL Rehab data for Patient Doe, John"

    # add processing for scores

    for person in email_list:

        # Make the body of the email
        body = f"""
        Dear Clinician,

        Attached as follows is the ACL Balance Monitoring Rehab data for Patient Doe, John 
        for the date of Wednesday, April 5th, 2023. 

        Please see above attachments for knee angle ROM's for each stage of the SEBT test 
        and foot center of mass deviations for each stage of the SEBT test. Each graph is 
        labeled correspondingly.

        The stability score regarding the knee angles 21 days post-op is calculated as: 
        {stability_score_angles}

        
        The stability score regarding the center of mass deviations 21 days post-op is calculated as: 
        {stability_score_CofM}

        Some extra details: 
        Center of Mass Standard Deviation Differences (X Direction)
        {SEBT_data_string_x}
        Center of Mass Standard Deviation Differences (Y Direction)
        {SEBT_data_string_y}

        Knee Angle Differences between Non-Operative and Operative Leg
        {SEBT_angle_diffs}

        Please contact the patie
         Thank you, 
         ReBalance Canada
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
# send_emails(email_list, ['sebt/Anterior_Non-Operative_SEBT_KneeAngles.png'], test_SEBT_data, test_CofM_data)
