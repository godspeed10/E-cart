from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

##SUPERUSER MODEL
class  MyAccountManager(BaseUserManager):

    ### Creating a normal user

    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            email = self.normalize_email(email),         ## normalize does what is that 
            username = username,                          ##  capital letters are changed to small letters   
            first_name = first_name,
            last_name = last_name,

        )
    
        user.set_password(password)
        user.save(using=self._db)
        return user
        ##############################################################################################################

        ## Creating  superuser

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user





## CUSTOM USER MODEL
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login  = models.DateTimeField(auto_now_add=True)
    is_admin    = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = MyAccountManager()                ## we need to tell account that we are using myaccount for the  all the obove create opertions


    def __str__(self):
        return self.email                      ## retrun email when we redner the tempplate
    
    def has_perm(self, perm, obj=None):
        return self.is_admin                     ## admin can change or update the things
    
    def has_module_perms(self, add_label):
        return True                 