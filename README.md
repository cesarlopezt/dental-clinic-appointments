# dental-clinic-appointments
Django website for a Project Management final project  

Setup:
1. `py venv env`
2. `env\Scripts\activate.bat`
3. `pip install -r requirements.txt`

First time running server:
1. `py manage.py migrate`
2. `py manage.py createsuperuser` and setup your admin credentials
4. Create `dev.py` file on `dental_clinic/settings/` with your desired settings, in case no new settings, just duplicate `base.py`
3. `py manage.py runserver --settings dental_clinic.settings.dev`
