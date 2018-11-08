from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Departamento(models.Model):
	codigoDepartamento = models.CharField(primary_key=True, max_length=15)
	nombreDepartamento = models.CharField(max_length=60)

	def __str__(self):
		return self.codigoDepartamento + ", " + self.nombreDepartamento

class Programa(models.Model):
	"""docstring for maestria"""
	codigoPrograma = models.IntegerField(primary_key=True)
	nombrePrograma = models.CharField(max_length=60)
	#codigoDepartamentoPertenece = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.codigoPrograma) + ", " + self.nombrePrograma

class Rol(models.Model):
	codigoRol = models.IntegerField(primary_key=True)
	nombreRol = models.CharField(max_length=60) # Profesor (2), Estudiante (3), Jefe del departamento (1)

	def __str__(self):
		return str(self.codigoRol) + ", " + self.nombreRol

class Asignatura(models.Model):
	codigoMateria = models.CharField(primary_key=True,max_length=7)
	nombreMateria = models.CharField(max_length=60)
	unidadesCredito = models.IntegerField()
	area = models.CharField(max_length=60) 
	programaPertenece = models.ForeignKey(Programa, on_delete=models.CASCADE)
	departamento = models.ForeignKey(Departamento, default="",on_delete=models.CASCADE)
	# Entre las areas segun el pdf se encuentran asignaturas basicas, inteligencia artificial
	# bases de datos entre otras
	def __str__(self):
		return self.codigoMateria + ", " + self.nombreMateria + ", " + str(self.unidadesCredito) + ", " + str(self.departamento_id) + ", " + str(self.programaPertenece_id) + ", " + self.area

class UserManager(BaseUserManager):
	"""Define a model manager for User model with no username field."""
	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		"""Create and save a User with the given email and password."""
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		"""Create and save a regular User with the given email and password."""
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		#extra_fields.setdefault('is_active', True)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		"""Create and save a SuperUser with the given email and password."""
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_active', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)

	

class User(AbstractBaseUser, PermissionsMixin):
	username = None
	email = models.EmailField(_('dirección de correo'), unique=True)
	is_staff = models.BooleanField(
		_('staff status'),
		default=False,
		help_text=_('Designates whether the user can log into this site.'),
	)
	is_active = models.BooleanField(
		_('active'),
		default=True,
		help_text=_(
			'Designates whether this user should be treated as active. '
			'Unselect this instead of deleting accounts.'
		),)
	is_superuser = models.BooleanField(
		_('superuser status'),
		default=False,
		help_text=_('Designates whether the user can log into this site.'),
	)
	#is_active = models.BooleanField(_('active'), default=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = UserManager()

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_short_name(self):
		'''
		Returns the short name for the user.
		'''
		return self.email

	def email_user(self, subject, message, from_email=None, **kwargs):
		'''
		Sends an email to this User.
		'''
		send_mail(subject, message, from_email, [self.email], **kwargs)
	

class Perfil(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	cedulaIdentidad = models.IntegerField(primary_key=True)
	primerNombre = models.CharField(max_length=15)
	segundoNombre = models.CharField(max_length=15, default="" ,blank = True)
	primerApellido = models.CharField(max_length=15)
	segundoApellido = models.CharField(max_length=15)
	rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
	codigoDepartamento1 = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	fechaRegistro = models.DateTimeField(_('fecha de registro'), auto_now_add=True)

	def __str__(self):
		return str(self.cedulaIdentidad) + ", "+ self.primerNombre+", "+ self.primerApellido +", "+ self.segundoApellido +", "+ str(self.rol_id) +", "+ self.codigoDepartamento1_id