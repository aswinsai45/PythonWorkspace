import datetime


class dateValidation:

    def validateDate(self, DOB):
        date_format = '%d/%m/%Y'
        isvalidDate = True
        try:
            datetime.datetime.strptime(DOB,date_format)
            return True
        except ValueError:
            return False
    def printtMyName(self):
        return "mynameIsSaiAswinRajaBokku"

d = dateValidation()
print(d.validateDate('31/11/2010'))
print(d.printtMyName())

