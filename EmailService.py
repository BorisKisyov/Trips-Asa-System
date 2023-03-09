from email.message import EmailMessage
import ssl
import smtplib

email_sender = "cameraserviceht@gmail.com"
email_password = "gaihwmihyentvwca"
email_reciever = ["martin.p.yordanov.2018@elsys-bg.org", "boris.e.kisyov.2018@elsys-bg.org", "nikola.p.petrov.2018@elsys-bg.org", "todor.b.kulchev.2018@elsys-bg.org", "stefan.s.kasamakov.2018@elsys-bg.org"]
subject = "Сигнал за сигурността на "
body = "There has been a security breach!"

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciever
em["Subject"] = subject
em.set_content(body)

# Load the PNG image
with open("image.png", "rb") as f:
    image_data = f.read()

# Add the image as a related part to the email
em.add_related(image_data, "image", "png")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
