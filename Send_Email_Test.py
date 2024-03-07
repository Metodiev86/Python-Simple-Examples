import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["From"] ="s.metodiev@stabil-di.com"
msg["To"] = "sto.metodiev86@gmail.com"
password = "smetodiev2023"
msg["Subject"] = "Python e-mail unity Test"
msg.set_content("Тестово съобщение")



server = smtplib.SMTP("smtp.stabil-di.com",587)
server.ehlo()
server.starttls()

try:
	server.login(msg["From"], password)
	print("Вие се логнахте")
	server.send_message(msg)
	print("Съобщението е изпратено!")
except smtplib.SMTPAuthenticationError:
	print("Проблем, не можахте да влезете в профила си!")

