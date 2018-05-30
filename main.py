import requests
import hashlib
import globals

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def send_points(receiver,amount):
	params = {"receiver":receiver,"amount":amount}
	r =  requests.post(url = URL+"/send_points", data = params)
	data = r.json()
	print("Status -> "+data["status"])
	print("Remaining balance -> "+data['points'])

def get_points():

def main():
	aadhar_num = raw_input("Enter your aadhar number")
	password = get_pass()
	password = hash_password(password)
	# URL = "localhost/get_points"

	params = {"aadhar":aadhar_num,"password":password}

	r = requests.post(url = URL+"/get_points", data = params)
	data = r.json()

	points = data['nature_points']
	print("You have :"+points+" points")

	while True:
		query = raw_input("So ?")
		if query == "q":
			return
		elif query == "s":
			print("Points :"+points)
		elif query == "n":
			# print(notifications)
		elif query == "t":
			receiver = raw_input("Enter the receiver's aadhar number")
			amount = raw_input("Amount to be sent")
			send_points(receiver,amount)



if __main__ == "__main__":
	main()