import psutil, sys
from tabulate import tabulate


approvedFlags = ["-h", "-l", "-v"]

def main():
	
	if len(sys.argv) == 1:
		print("usage: python processKilla.py [-h help] [-l List Processes] [-n Process Name string] [-v Verbose]")
	elif len(sys.argv) > 1:
		if unapprovedFlags():
			print("Unapproved flags used - use \"python processKilla.py -h\" for help")
			return(0)

	elif sys.argv[1] == "-h":
		print("Help im lost")

	elif "-l" in sys.argv:
		table = []
		if "-v" in sys.argv:
			table.append(["Process ID", "Process Name"])
			for proc in psutil.process_iter():
				try:	
										
					processName = proc.name()
					processID = proc.pid
					table.append([processID, processName])
					print(dir(proc	))
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



def unapprovedFlags():
	result = False
	for flag in sys.argv:
		if not flag in approvedFlags:
			result = True
	return result



if __name__ == "__main__":
	#Execute only if run as a script
	main()