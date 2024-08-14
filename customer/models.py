from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='customers/')

    @property
    def get_initial(self):
        first_initial = self.first_name[0] if self.first_name else ''
        last_initial = self.last_name[0] if self.last_name else ''
        return f'{first_initial.upper()} {last_initial.upper()}'

    @property
    def joined_at(self):
        return self.created_at.strftime('%Y-%m-%d')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.full_name} {self.email} {self.phone} {self.address}'
