from django.db import models
from django.core.mail import send_mail
from twilio.rest import Client
from django.contrib.auth.hashers import make_password
import secrets
import string

# from django.db import models

class Farmers(models.Model):
    id = models.AutoField(primary_key=True)
    farmer_name = models.CharField(max_length=15)
    bank_name = models.CharField(max_length=15)  # Renamed to follow Python naming conventions
    bank_account = models.DecimalField(max_digits=10, decimal_places=0)
    type_of_crops = models.CharField(max_length=25)
    quant_of_products = models.FloatField()
    total_cost_production = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=13)
    location = models.CharField(max_length=15)
    year = models.IntegerField()

    def __str__(self):
        return self.farmer_name  # String representation for Farmer model

class FarmDetails(models.Model):
    id = models.AutoField(primary_key=True)
    owner_of_farm = models.CharField(max_length=15)
    size_of_farm = models.CharField(max_length=10)
    no_of_farms = models.DecimalField(max_digits=20, decimal_places=0)
    assets_available = models.CharField(max_length=15)
    physical_location = models.CharField(max_length=15)

    def __str__(self):
        return self.owner_of_farm  # String representation for FarmDetails model

class Crops(models.Model):
    crop_id = models.AutoField(primary_key=True)
    crop_name = models.CharField(max_length=30)
    crop_owner = models.ForeignKey(Farmers, on_delete=models.CASCADE)  # Foreign key to Farmers model
    quant_of_crops = models.IntegerField()

    def __str__(self):
        return self.crop_name  # String representation for Crops model



class Amkosi(models.Model):
    assoc_name = models.CharField(max_length=25, primary_key=True)
    assoc_email = models.CharField(max_length=30)
    assoc_password = models.CharField(max_length=128, unique=True)  # Storing hashed password
    location = models.CharField(max_length=12)
    assoc_phone_no = models.CharField(max_length=13)

    def generate_unique_password(self):
        # Generate a unique password using secrets module
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(12))  # Modify the length of the password here
        hashed_password = make_password(password)
        return hashed_password

    def send_password_via_sms(self, password):
        # Twilio SMS sending logic
        account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
        auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
        twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'

        client = Client(account_sid, auth_token)

        try:
            message = client.messages.create(
                body=f'Hello {self.assoc_name}, your new password is: {password}',
                from_=twilio_phone_number,
                to=self.assoc_phone_no
            )
            print(f"SMS sent successfully to {self.assoc_phone_no}")
            return True
        except Exception as e:
            print(f"Failed to send SMS: {str(e)}")
            return False

    def send_password_via_email(self, password):
        # Django's send_mail function to send email
        subject = 'Your New Password'
        message = f'Hello {self.assoc_name},\n\nYour new password is: {password}\n\nPlease keep it secure.'
        from_email = 'your@example.com'  # Replace with your email
        recipient_list = [self.assoc_email]

        send_mail(subject, message, from_email, recipient_list)

    def save(self, *args, **kwargs):
        if not self.assoc_password:
            self.assoc_password = self.generate_unique_password()

            # Send password via SMS
            self.send_password_via_sms(self.assoc_password)

            # Send password via Email
            self.send_password_via_email(self.assoc_password)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.assoc_name
