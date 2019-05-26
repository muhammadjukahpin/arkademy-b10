import re
def is_username_valid(username):
	username_pattern = re.compile("^([a-z]{8})")
	if username_pattern.match(username):
		print(True)
	else:
		print(False)

def is_email_valid(email):
	password_pattern = re.compile("^([a-zA-Z0-9\.]){4}@[a-zA-Z]+\.[a-zA-Z]+")
	if password_pattern.match(email):
		print(True)
	else:
		print(False)

is_username_valid("zeronull")
is_email_valid("aku@kamu.com")
is_email_valid("kamu@aku.com")