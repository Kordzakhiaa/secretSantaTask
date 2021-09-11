import smtplib


EMAIL_ADDRESS = 'test.userr2001@gmail.com'
EMAIL_PASSWORD = 'Giorgi55'


def sent_mail(giver_reciever: list):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'Secret Santa By Kordzakhia'
        body = 'You have to give a gift'

        for dictionary in giver_reciever:
            for sender, reciever in dictionary.items():
                msg = f'Subject: {subject}\n\n{body} to {reciever}'
                smtp.sendmail(EMAIL_ADDRESS, sender, msg)
