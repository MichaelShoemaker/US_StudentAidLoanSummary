principle = 0
total = 0

with open('MyStudentAid.txt','r') as infile:
    for line in infile:
        if 'Loan Disbursed Amount' in line:
            principle += float(line.split('$')[-1].replace(',',''))
        if 'Loan Cumulative Payment Amount' in line:
            total += float(line.split('$')[-1].replace(',',''))

interest = total-principle
print(f"Total amount disbursed was -- ${principle:,.2f}")
print(f"Total amount with interest paid was -- ${total:,.2f}")
print(f"You paid a total of -- ${total-principle:,.2f} in interest alone")
print(f"That acounts for -- {round(interest/total,4)*100}% -- of your total amount paid")
print(f"and is equivelant to -- {round(interest/principle,4)*100}% -- of your original loan amount")
print('********MERICA!!!!*********')
