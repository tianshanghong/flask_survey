# -*- coding: utf-8 -*-

from flask.ext.wtf import Form, fields, validators, Required, Email, Regexp
from models import User
from app import db


def validate_login(form, field):
    user = form.get_user()
    if user is None:
        raise validators.ValidationError('Invalid user')
    if user.password != form.password.data:
        raise validators.ValidationError('Invalid password')


class LoginForm(Form):
    email = fields.TextField(validators=[Required(), Email()])
    password = fields.PasswordField(validators=[Required(), validate_login])

    def get_user(self):
        return db.session.query(User).filter_by(email=self.email.data).first()


class ForgotPasswordForm(Form):
    email = fields.TextField(validators=[Required(), Email()])

    def get_user(self):
        return db.session.query(User).filter_by(email=self.email.data).first()


class RegistrationForm(Form):
    email = fields.TextField('Email Address',
        validators=[Required(), Email(), Regexp('[^@]+@[^@]+[fsu]+\.[edu]+')])
    consent = fields.BooleanField(validators=[Required()])
    password = fields.PasswordField('New Password', [
        validators.Required(), validators.Length(min=8, max=20),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = fields.PasswordField(validators=[Required()])

    def validate_email(self, field):
        if db.session.query(User).filter_by(email=self.email.data).count() > 0:
            raise validators.ValidationError('Duplicate email')


class NewPass(Form):
    password = fields.PasswordField('New Password', [
        validators.Required(), validators.Length(min=8, max=20),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = fields.PasswordField(validators=[Required()])


class Survey1Form(Form):
    gender = fields.RadioField('What is your gender?',
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'I prefer not to answer')],
        validators=[Required()], default=None)
    age = fields.RadioField('What is your age?',
        choices=[('lt18', 'Younger than 18'), ('18-24', '18 to 24'), ('25-34', '25 to 34'),
            ('35-44', '35 to 44'), ('45-54', '45 to 54'), ('55', '55 years or older')],
        validators=[Required()])
    education = fields.RadioField('Which of the following best describes your highest education level?',
        choices=[('Hsg', 'High school graduate'),
            ('Scnd', 'Some college, no degree'), ('Assoc', 'Associates Degree'),
            ('Bach', 'Bachelors degree'), ('Grad', 'Graduate degree (Masters, Doctorate, etc.)'),
            ('O', 'Other')],
        validators=[Required()])
    language = fields.TextField('What is your native language', validators=[Required()])


class Survey2Form(Form):
    major = fields.RadioField('Are you majoring in or do you have a degree or job in computer science, computer engineering, information technology, or a related field?',
        choices=[('Y', 'yes'), ('N', 'No'), ('O', 'I prefer not to answer')],
        validators=[Required()])
    count = fields.RadioField('How many website user-names and passwords do you have, approximately?',
        choices=[('lt5', 'Less than 5 accounts'),
            ('5-10', '5 to 10 Accounts'), ('11-20', '11 to 20 Accounts'),
            ('gt20', 'More Than 20 Accounts')])
    unique = fields.RadioField('Do you try to create unique passwords for each different account?',
        choices=[('Y', 'Yes, I create a new password every time I create a new account or every time I have to change my password'),
            ('N', 'No, I use my old passwords that I have already created for my other accounts'),
            ('O', 'I mostly create a new password, but sometimes use old passwords')],
        validators=[Required()])
    department = fields.TextField('In what department are you majoring', validators=[Required()])


class Survey3Form(Form):
    choose_names = fields.BooleanField('Names of family members, relatives, close friends')
    choose_numbers = fields.BooleanField('Familiar numbers (birth date, telephone number, street address, employee number, etc.)')
    choose_songs = fields.BooleanField('Songs, movies, television shows, books, poetry or games')
    choose_mnemonic = fields.BooleanField('Scientific or other educational mnemonics')
    choose_sports = fields.BooleanField('Sports teams and players')
    choose_famous = fields.BooleanField('Names of famous people or characters')
    choose_words = fields.BooleanField('Words in a language other than English')
    choose_other = fields.BooleanField('other')
    specify = fields.TextField('please specify')
    secure_numbers = fields.BooleanField('Include numbers')
    secure_upper_case = fields.BooleanField('Include upper case letters')
    secure_symbols = fields.BooleanField('Include symbols(such as "!" or "#")')
    secure_eight_chars = fields.BooleanField('Have 8 or more characters')
    secure_no_dict = fields.BooleanField('Not contain dictionary words')
    secure_adjacent = fields.BooleanField('Not containing a sequence of adjacent or repeated characters on your keyboard (e.g. qwerty)')
    secure_nothing = fields.BooleanField('I did not consider any policy')
    secure_other = fields.BooleanField('other')
    specify1 = fields.TextField('please specify')
    modify = fields.RadioField('Did you create your new password by slightly changing your old password for this website?',
        choices=[('Y', 'Yes'), ('N', 'No')],
        validators=[Required()], default=None)
    usedPassword = fields.RadioField('Is the password that you have just created one that you have used in the past?',
        choices=[('Y', 'Yes'), ('N', 'No'), ('O', 'Password has similarities to another password that I have used before')],
        validators=[Required()], default=None)
    number_N = fields.BooleanField('Not changed')
    number_changed_slightly = fields.BooleanField('Changed Slightly')
    number_changed_completly = fields.BooleanField('Changed Completely')
    number_added_digits = fields.BooleanField('Added Digits')
    number_deleted_digits = fields.BooleanField('Deleted Digits')
    char_N = fields.BooleanField('Not Changed')
    char_changed_slightly = fields.BooleanField('Changed Slightly')
    char_changed_completly = fields.BooleanField('Changed Completly')
    char_added_symbols = fields.BooleanField('Added Symbols')
    char_deleted_symbols = fields.BooleanField('Deleted Symbols')
    not_changed1 = fields.BooleanField('Not changed')
    changed_slightly1 = fields.BooleanField('Changed Slightly')
    changed_completly1 = fields.BooleanField('Changed completely')
    capatalized1 = fields.BooleanField('Capatlized or lower case letters')
    addedwords = fields.BooleanField('Added Words or Letters')
    deletedwords = fields.BooleanField('Deleted Words or Letters')


class Survey4Form(Form):
    computerTime = fields.RadioField('How long have you been using a computer?',
        choices=[('0-2', '0 to 2 Years'), ('3-5', '3 to 5 Years'), ('6-10', '6 to 10 Years'),
            ('mt10', 'More than 10 years')],
        validators=[Required()], default=None)
    pass_random = fields.BooleanField('Randomly generate a password using special software or apps')
    pass_reuse = fields.BooleanField('Reuse a password that is used for another account')
    pass_modify = fields.BooleanField('Modify a password that is used for another account')
    pass_new = fields.BooleanField('Create a new password using a familiar number or a name of a family member')
    pass_substitute = fields.BooleanField('Choose a word and substitute some letters with numbers of symbols (for example @ for a)')
    pass_multiword = fields.BooleanField('Use a pass-phrase consisting of several words')
    pass_phrase = fields.BooleanField('Choose a phrase and use the first letters of each word')
    pass_O = fields.TextAreaField('Other')
    how_regular_file = fields.BooleanField('I store my passwords in a regular file / document on my computer.')
    how_encrypted = fields.BooleanField('I store my passwords in an encrypted computer file')
    how_software = fields.BooleanField('I use password management software to securely store my passwords')
    how_cellphone = fields.BooleanField('I store my passwords on my cellphone / smartphone')
    how_browser = fields.BooleanField('I save my passwords in the browser')
    how_write_down = fields.BooleanField('I write down my password on a piece of paper')
    how_no = fields.BooleanField('No, I do not save my passwords. I remember them.')
    comments = fields.TextAreaField('If you have any additional feedback about passwords or this survey, please enter your comments here.', default=None)