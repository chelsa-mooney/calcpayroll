from tabulate import tabulate

employee_details = 10

while employee_details > 10:

	#employee information 
	employee_name = input("Name: ")

	#income 
	pay_rate = int(input("Hourly pay: "))
	hours_worked= int(input("Hours worked: "))
	ot_pay = int(input("Overtime hours: "))

	#gross pay
	gross_pay = pay_rate * hours_worked

	#witholdings
	fed_tax = gross_pay * .12
	state_tax = gross_pay * 0.03
	fica = gross_pay * 0.062


	#if overtime
	ot_pay < 0
	overtime_pay = (pay_rate * 1.5) * ot_pay
	ot_pay = overtime_pay 

	#net pay
	net_pay = (ot_pay + gross_pay)  - (fed_tax + state_tax + fica)

	print(f"You worked", str(hours_worked) + " hours")
	print(f"Pay rate: ${pay_rate}")
	print(f"Gross pay: ${gross_pay}")
	print(f"Overtime pay: ${ot_pay}")
	print(f"Federal tax: ${fed_tax}")
	print(f"State tax: ${state_tax}")
	print(f"FICA: ${fica}")
	print(f"Net pay: ${net_pay}")

	print(tabulate([["Employee Name", "Pay Rate", "Hours Worked", "OT Pay", "Gross Pay", 
"Fed Tax", "State Tax", "FICA", "Net Pay"], [employee_name, pay_rate, hours_worked, 
ot_pay, gross_pay, fed_tax, state_tax, fica, net_pay]]))

