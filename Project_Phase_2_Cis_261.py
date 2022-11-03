#Ezra Felton CIS 261 Corse Progect 1


def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

def GetHoursWorked():
    hoursworked = float(input("Enter amount of hours worked:  "))
    return hoursworked

def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate:  "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input("Enter tax rate:   "))
    return taxrate
#______________________________________________________________________________________

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print(empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")

def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours: {TotHours:,.2f}")
    print(f"Total Pay: {TotGrossPay:,.2f}")
    print(f"Total Tax: {TotTax:,.2f}")
    print(f"Total Net: {TotNetPay:,.2f}")

def printTotHours(TotHours, TotGrossPay, TotTax, TotNetpay):
    print(f"{TotHours:,.2f}", f"{TotGrossPay:,.2f}", f"{TotTax:,.2f}", f"{TotNetPay:,.2f}" )

    # write the code to print TotHours, TotGrossPay, TotTax, and TotNetpay with 2 decimal places+++++++++++

#__________________________________________________________________________________________
if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        hours = GetHoursWorked()
       
        hourlyrate = GetHourlyRate()
        
        taxrate = GetTaxRate()
       
        # write the code to assign to hours the return value from GetHoursWorked+++
        # write the code to assign to hourlyrate the return value from GetHourlyRate+++
        # write the code to assign to taxrate the return value from GetTaxRate+++
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay

        # write the code to increment the other total variables with the appropriate values

    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
