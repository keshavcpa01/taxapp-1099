import base64

import sendgrid
from fpdf import FPDF
from sendgrid.helpers.mail import Attachment, Mail

SENDGRID_API_KEY = "your-sendgrid-api-key"
FROM_EMAIL = "noreply@yourdomain.com"

def generate_pdf(submission):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="1099 Submission Confirmation", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Payer: {submission.payer_name}", ln=True)
    pdf.cell(200, 10, txt=f"Recipient: {submission.recipient_name}", ln=True)
    pdf.cell(200, 10, txt=f"Amount: {submission.amount}", ln=True)
    pdf.output("confirmation.pdf")
    with open("confirmation.pdf", "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    return encoded

def send_confirmation_email_with_pdf(to_email, submission):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    pdf_data = generate_pdf(submission)
    attachment = Attachment()
    attachment.content = pdf_data
    attachment.type = "application/pdf"
    attachment.filename = "1099_confirmation.pdf"
    attachment.disposition = "attachment"

    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject="Your 1099 Submission Confirmation",
        html_content="<strong>Thank you for your submission.</strong>",
    )
    message.attachment = attachment
    sg.send(message)
