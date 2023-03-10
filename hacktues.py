from email.message import EmailMessage
import ssl
import smtplib
import glob
import os

email_sender = "cameraserviceht@gmail.com"
email_password = "gaihwmihyentvwca"
email_reciever = ["todor.b.kulchev.2018@elsys-bg.org", "martin.p.yordanov.2018@elsys-bg.org", "boris.e.kisyov.2018@elsys-bg.org", "nikola.p.petrov.2018@elsys-bg.org", "stefan.s.kasamakov.2018@elsys-bg.org"]
subject = "Сигнал за сигурността на "
body = "There has been a security breach!"

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciever
em["Subject"] = subject
em.set_content(body)

# Get a list of image files in the directory
image_files = glob.glob("*.png")

# Check if there are any image files in the directory
if image_files:
    # Sort the list of image files by modification time
    image_files.sort(key=lambda x: os.path.getmtime(x))

    # Get the last image file in the list
    last_image = image_files[0]

    # Load the last image file
    with open(last_image, "rb") as f:
        image_data = f.read()

    # Add the image as a related part to the email
    em.add_related(image_data, "image", "png")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())

else:
    print("No image files found in the directory.")