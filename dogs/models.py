from random import choices
from django.db import models
from datetime import datetime
from django.utils import timezone
from datetime import timedelta
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from phone_field import PhoneField


# Create your models here.
def one_month_from_today():
    return timezone.now() + timedelta(days=30)



class Dog(models.Model):

    state_choice = (
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('UP', 'Uttar Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CG', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Orissa'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TR', 'Tripura'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DH', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'),
        ('DL', 'Delhi'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Pondicherry'),
        
    )

    

    features_choices = (
        ('KCI Registerd', 'KCI Registerd'),
        ('Guard Dog', 'Guard Dog'),
        ('India Dog Show Winner', 'India Dog Show Winner'),
        ('Russian Champion', 'Russian Champion'),
        
    )

    Dog_Gender = (
        ('male', 'male'),
        ('female', 'female'),
        
    )

    kci_choices = (
        ('yes', 'yes'),
        ('no', 'no'),
        
    )

    pet_size = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large','Large'),
        ('Extra Large','Extra Large'),
        
    )

    Energy_Level = (
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('High','High'),
        
    )
    
    Friendliness_choices = (
        ('Toward Dogs', 'Toward Dogs'),
        ('Towards Other Pets', 'Towards Other Pets'),
              
    )

    Dog_type = (
        ('Adult', 'Adult'),
        ('Pups', 'Pups'),
              
    )

    EASE_OF_TRAINING = (
        ('Easy', 'Easy'),
        ('Average', 'Average'),
        ('Difficult','Difficult'),
        
    )

    Grooming_Requirements = (
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('High','High'),
        
    )

    Vocality = (
        ('Low','Low'),
        ('Moderate','Moderate'),
        ('High','High'),
    )

    Exercise_Requirement = (
        ('Moderate','Moderate'),
        ('Significant','Significant'),
        ('Rigorous','Rigorous'),
    )
    
    Affection_Need = (
        ('Independant','Independant'),
        ('Balanced','Balanced'),
        ('Cuddly','Cuddly'),
    )


    def age(self):
            import datetime
            dob = self.date_of_birth
            tod = datetime.date.today()
            my_age = (tod.year - dob.year) - int((tod.month, tod.day) < (dob.month, dob.day))
            return my_age


    bread_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=datetime.today)
    age = models.DateField(default=one_month_from_today, blank=True, null=True)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    gender = models.CharField(choices=Dog_Gender, max_length=100,default='Litter')
    KCI_Registerd = models.CharField(choices=kci_choices,max_length=100,default='No Information')
    Dogs_type = models.CharField(choices=Dog_type, max_length=100,default='pups')
    price = models.IntegerField()
    description = RichTextField()
    bread_size = models.CharField(choices=pet_size,max_length=100,default='No Information')
    Energy_Levels = models.CharField(choices=Energy_Level,max_length=100,default='Moderate') 
    dog_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    dog_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    dog_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    dog_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    dog_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices)
    aggresive = models.CharField(choices=Friendliness_choices, max_length=100,default='No Information')
    Training = models.CharField(choices=EASE_OF_TRAINING, max_length=100,default='No Information')
    Hair_Grooming = models.CharField(choices=Grooming_Requirements,max_length=100,default='Not Required')
    aggresive = models.CharField(choices=Vocality,max_length=100,default='No Information')
    Exercise = models.CharField(choices=Exercise_Requirement,max_length=100,default='Significant')
    affection_with_family = models.CharField(choices=Affection_Need,max_length=100,default='How much you love your dogs')
    breader_name = models.CharField(max_length=255,default='No Information')
    breader_contact = PhoneField(blank=True, help_text='Contact phone number',default='No Information')
    #age = models.DateTimeField(property(age),default=datetime.now)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.bread_name