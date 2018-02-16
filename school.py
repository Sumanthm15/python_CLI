import mysql.connector
import sys
cnxn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",db = "school")
cursor = cnxn.cursor()

class p(Exception):
	pass

class r(Exception):
	pass

class ch_id(Exception):
	pass		
	
class index_form:

	def ss_form(self):

		print("-----------------------------------------------------------------------")
		print("1. Signup")
		print("2. Signin\n")

		while True:
			i = int(input("Please choose the number: "))
			print("-----------------------------------------------------------------------")

			if i == 1:
				self.f_signup()
				break

			elif i == 2:
				self.f_signin()
				break

			else:
				print("Please Try again")
				print("-----------------------------------------------------------------------")
				continue

	def f_signup(self):

		while True:

			try:
				a_id = int(input("Please enter your id: "))
				
				args = (a_id,0)
				res = cursor.callproc('check_id',args)
				
				if res[1]>0:
					raise ch_id

				else:
					f_id = a_id

				f_name = input("Please enter your full name: ")
				f_pwd = input("New password: ")
				f_pwd1 = input("Confirm password: ")

				if f_pwd != f_pwd1:
					raise p

				else:
					pwd = f_pwd

				print("Choose \nm. Management \nt. Teacher \ns. Student")

				role = (input("Enter the role: ")).lower()

				if (role != 'm') and (role != 't') and (role != 's'):
					raise r

				else:

					if role == 't':
						sub = input("Enter your subject: ")

					elif role == 's':
						dep = input("Enter your department: ")

				if role == 'm':
					args = (f_id,f_name,pwd)
					cursor.callproc('insert_management', args)
					print("-----------------------------------------------------------------------")
					print("Successfully Created the Management account")
					print("-----------------------------------------------------------------------")
					self.re_sign()
				

				elif role == 't':
					args = (f_id,f_name,pwd,sub)
					cursor.callproc('insert_teacher', args)
					print("-----------------------------------------------------------------------")
					print("Successfully Created the Teacher account")
					print("-----------------------------------------------------------------------")
					self.re_sign()
				
					
				elif role == 's':
					args = (f_id,f_name,pwd,dep)
					cursor.callproc('insert_student', args)
					print("-----------------------------------------------------------------------")
					print("Successfully Created the Student Account")
					print("-----------------------------------------------------------------------")
					self.re_sign()
				

			except ValueError:
				print("ID should be an Integer")
				print("-----------------------------------------------------------------------")
				continue

			except p:
				print("These passwords don't match. Try again!")
				print("-----------------------------------------------------------------------")
				continue

			except r:
				print("Please enter the correct role")
				print("-----------------------------------------------------------------------")
				continue

			except ch_id:
				print("ID already exists")
				print("-----------------------------------------------------------------------")
				continue

			else:
				break

			finally:
				pass
											
	def f_signin(self):

		while True:

			try:
				f_id = int(input("Enter your id: "))
				pwd = input("Enter password: ")
				print("-----------------------------------------------------------------------")

				args = [f_id,pwd,0]
				result_args = cursor.callproc('confirm', args)
				#we should not declare the out parameter given in the create procedure statement in stored procedure
				if result_args[2] == 'm':
					print("Welcome to the Management Account")

				elif result_args[2] == 't':
					print("Welcome to the Teacher Account")

				elif result_args[2] == 's':
					print("Welcome to the Student Account")
				else:
					print("There were errors in your submission. Please try again!")
					print("-----------------------------------------------------------------------")
					continue

				self.re_sign()

			except ValueError:
				print("ID should be an Integer")
				print("-----------------------------------------------------------------------")
				continue

			else:
				break

			finally:
				pass

	def re_sign(self):

		while True:
			
			try:
				print("-----------------------------------------------------------------------")
				ans = (input("Do you want to continue (Y/N): ")).lower()

				if (ans == 'yes') or (ans == 'y'):
					self.ss_form()
				elif (ans == 'no') or (ans == 'n'):
					sys.exit(0)
				else:
					raise p					

			except p:
				print("-----------------------------------------------------------------------")
				print("Invalid! Please enter correct input")
				print("-----------------------------------------------------------------------")
				continue
			finally:
				pass

				
obj = index_form()
obj.ss_form()

cnxn.commit()
cnxn.close()