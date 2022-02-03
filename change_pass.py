import getpass
from main import *

print("Chagne Admin password For security")

try:
	olduname = input(str("enter last username: "))

	username = input(str("enter your username: "))

	password = getpass.getpass(prompt="enter your password: ")

	c_password = getpass.getpass(prompt="confirm your password: ")
except Exception as e:
	raise e

if (password == c_password):
	admin = Admin.query.filter_by(name=olduname).first()
	print(admin)
	hass_pass = bcrypt.generate_password_hash(password).decode('utf-8')
	admin.name = username
	admin.password = hass_pass
	db.session.commit()
	print("password changed")
else:
	print("password did not match, please try again")