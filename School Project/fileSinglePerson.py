import singleperson

print('Generating ticket..')
print("~~~YOUR TICKET HAS BEEN BOOKED SUCCESSFULLY. YOUR TICKET NUMBER IS AX", str(singleperson.boardGen), "~~~")
f = open("C:/Users/aswin/PycharmProjects/School Project/AirReservation_Project/BookingConf/" + 'AX' + str(singleperson.boardGen),
         'a+')
f.write('PASSENGER 1: ' + '\n')
f.write(
    'Name: ' + singleperson.passenger1 + '\n' + 'Date of Birth: ' + singleperson.DOB + '\n' 'Passport Number: ' + singleperson.passportNumber + '\n' 'Expiry Date : ' + singleperson.passportExpiry + '\n')
f.write('Your Journey is on: ' + singleperson.travelDate + '\n')
f.write('Airline: ' + singleperson.airline_Timing.listofairlines[singleperson.airline_Timing.airline] + ' | ' + 'Aircraft Number: ' + str('A320 - ' +
    singleperson.flightGen) + '|')
f.write(
    'Departure: ' + singleperson.departureCity + ', ' + singleperson.departureCountry + '  |  ' + 'Destination: ' + singleperson.destinationCity + ', ' + singleperson.destinationCountry + '\n')

f.write("Your Boarding Pass Number is AX" + str(singleperson.boardGen))
f.close()
exit()
