from django.conf import settings
from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse
from model_mommy import mommy
from django.contrib.auth import get_user_model
from core.forms import ContactForm

User = get_user_model()


class IndexTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET / Must return status code 200"""
        self.assertEquals(200, self.response.status_code)

    def test_template_used(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')


class TestContactForm(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('contact')
        self.response = self.client.get(self.url)

    def test_view_ok(self):
        self.assertEquals(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 'contact.html')

    def test_form_errors(self):
        data = {'name': '', 'email': '', 'message': ''}
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')

    def test_html(self):
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 3)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf_token(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, ContactForm) 

    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'email', 'message'], list(form.fields))


class TestContactFormPass(TestCase):

    def setUp(self):
        self.url = reverse('contact')
        self.data = dict(name='Kelver Alves', email='kelverwt@gmail.com',
                         message='Hello, World!')
        self.response = self.client.post('contact', self.data)

    def test_subscription_send_email(self):
        self.response = self.client.post(self.url, self.data)
        self.assertEqual(len(mail.outbox), 1)

    def test_subscription_email_subject(self):
        self.response = self.client.post(self.url, self.data)
        self.assertEquals(mail.outbox[0].subject, 'Confirmação de contato')


class TestLogin(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('1234')
        self.user.save()

    def tearDown(self):
        self.user.delete()


    def test_login_ok(self):
        """LOGIN / must return status code 200"""
        self.response = self.client.get(self.login_url)
        self.assertEquals(200, self.response.status_code)
        data = dict(username=self.user.username, password='1234')
        response = self.client.post(self.login_url, data)
        redirect_url = reverse(settings.LOGIN_REDIRECT_URL)
        self.assertRedirects(response, redirect_url)

    def test_template_used(self):
        self.response = self.client.get(self.login_url)
        self.assertTemplateUsed(self.response, 'login.html')

    def test_error_login(self):
        data = {'username': self.user.username, 'password': '12345'}
        response = self.client.post(self.login_url, data)
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'login.html')
        error_mgs = ('Por favor, entre com um Apelido / Usuário e senha corretos. Note que ambos os campos diferenciam maiúsculas e minúsculas.')

    def test_user_is_not_loged(self):
        #data = {'username': self.user.username, 'password': '1234'}
        response = self.client.post(self.login_url)
        self.assertTrue(not response.wsgi_request.user.is_authenticated)

    def test_user_is_loged(self):
        data = {'username': self.user.username, 'password': '1234'}
        response = self.client.post(self.login_url, data)
        self.assertTrue(response.wsgi_request.user.is_authenticated)


class TestRegisterOk(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_register_ok(self):
        data = {'username': 'kelver', 'password1': 'teste1234', 'password2': 'teste1234'}
        response = self.client.post(self.register_url, data)
        index_url = reverse('login')
        self.assertRedirects(response, index_url)
        self.assertSetEquals(User.objects.count(), 1)