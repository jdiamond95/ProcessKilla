import psutil, sys
from tabulate import tabulate


approvedFlags = ["-h", "-l", "-v"]

def main():

	#Check whether any flags are incorrectly used - recommend help if so
	if len(sys.argv) > 1:
		if unapprovedFlags():
			print("Unapproved flags used - use \"python processKilla.py -h\" for help")
			return(0)

	#No flags, help
	if len(sys.argv) == 1:
		print("usage: python processKilla.py [-h help] [-l List Processes] [-n Process Name string] [-v Verbose]")
	
	#Help flag
	elif "-h" in sys.argv:
		print("usage: python processKilla.py [-h help] [-l List Processes] [-n Process Name string] [-v Verbose]")

	elif "-l" in sys.argv:
		printProcessList()


def unapprovedFlags():
	result = False
	for flag in sys.argv[1:]:
		if not flag in approvedFlags:
			result = True
	return result


def printProcessList():
	table = []

	#Verbose flag used, provide more process info
	if "-v" in sys.argv:
		table.append(["Process ID", "Process Name"])
		for proc in psutil.process_iter():
			try:						
				processName = proc.name()
				processID = proc.pid
				# threads = proc.threads()
				exe = proc.exe()
				table.append([processID, processName, exe])
			except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
				pass

	else:
		for proc in psutil.process_iter():
			try:
				processName = proc.name()
				processID = proc.pid
				table.append([processID, processName])
			except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
				pass

	print(tabulate(table))


if __name__ == "__main__":
	#Execute only if run as a script
	main()