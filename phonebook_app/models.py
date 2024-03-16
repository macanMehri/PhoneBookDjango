from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(
        default=False,
        verbose_name='Is Active'
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created Date'
    )

    updated_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated Date'
    )

    class Meta:
        abstract = True
    

    def __str__(self) -> str:
        raise NotImplementedError('You did not override the string method!')


class Address(BaseModel):
    country = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Country'
    )

    city = models.CharField(
        max_length=255,
        null=False,
        verbose_name='City'
    )

    exact_location = models.TextField(
        verbose_name='Exact location'
    )

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
    

    def __str__(self) -> str:
        return f'{self.city} in {self.country} - {self.exact_location}'


class Person(BaseModel):

    first_name = models.CharField(
        max_length=255,
        null=False,
        verbose_name='First Name'
    )
    
    last_name = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Last Name'
    )

    number = models.CharField(
        max_length=12,
        null=False,
        verbose_name='Phone Number'
    )

    address = models.ForeignKey(
        Address,
        on_delete=models.deletion.PROTECT,
        null=False,
        verbose_name='Address'
    )

    
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


    def __str__(self) -> str:
        return f'{self.full_name} - {self.number} - {self.address}'
