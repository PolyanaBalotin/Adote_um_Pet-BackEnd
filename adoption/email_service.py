from django.core.mail import send_mail


def send_confirmation_email(adoption):
    subject = "Adoção realizada com sucesso!"
    content = f"Parabéns por realizar a adoção do pet {adoption.pet.name} com o valor mensal de {adoption.value}"
    sender = "polybalotin@gmail.com"
    recipient = [adoption.email]
    send_mail(subject, content, sender, recipient)
