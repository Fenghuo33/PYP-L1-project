import file_utils as util

def view_medical_records(id):
    record = util.search_in_file("medical_record.txt", id = id)
    if record:
        user_id, diagnosis, prescriptions, treatment_plan = record[0]
    else:
        print(f'Error: No medical record with id: {id} found, please check with your receptionist')
        return
    print(f'Diagnosis: {diagnosis}, Treatment plan: {treatment_plan}')
    input("Press Enter to continue...\n")

def view_appointments(id):
    appointments = util.search_in_file("appointments.txt", patient_id = id)
    if not appointments:
        print(f'No Appointment with id: {id} found, please check with your receptionist')
        return
    print("------------------------------\n"
          "Your future appointments\n"
          "------------------------------")
    count = 1
    for appointment in appointments:
        patient_id, doctor_id, date, time = appointment
        doctor_name = util.search_in_file("doctor.txt", id=doctor_id)[0][1]
        print(f'{count}. Date: {date}, Time: {time}, Doctor: {doctor_name}')
        count += 1
    input("Press Enter to continue...\n")

def update_info(id):
    result = util.search_in_file("patient.txt", id = id)
    if result:
        user_id, name, DOB, gender, contact, address, medical_history = result[0]
    else:
        print(f'Error: No patient with id: {id} found, please check with your receptionist')
        return
    while True:
        print(f'1. Name: {name}\n'
              f'2. Date of Birth: {DOB}\n'
              f'3. Gender: {gender}\n'
              f'4. Contact: {contact}\n'
              f'5. Address: {address}\n'
              f'6. Confirm update \n'
              f'7. Undo update')
        choice = input("Choose which to update: ")
        match choice:
            case '1':
                new_name = input("Enter your name: ")
                name = new_name
            case '2':
                new_DOB = input("Enter your birth year: ")
                DOB = new_DOB
            case '3':
                new_gender = input("Enter your gender: ")
                gender = new_gender
            case '4':
                new_contact = input("Enter your new contact: ")
                contact = new_contact
            case '5':
                new_address = input("Enter your new address: ")
                address = new_address
            case '6':
                confirm = input("Are you sure to proceed (update can't be reverted, y for yes): ")
                if confirm.lower() == 'y':
                    util.update_file('patient.txt', {'name':name,'age':age,'gender':gender,'contact':contact,'address':address},{'id':user_id})
                break
            case '7':
                break



def view_payment(id):
    payments = util.search_in_file("payment.txt", patient_id = id)
    if not payments:
        print(f'Error: No Payment with id: {id} found, please check with your receptionist')
        return
    print("------------------------------\n"
          "Your payment history\n"
          "------------------------------")
    count = 1
    for payment in payments:
        payment_id, total_price, patient_id, status, payment_date = payment
        print(f'{count}. Total price: {total_price}, Status: {status}', end = "")
        print(f', Payment date: {payment_date}') if payment_date else print("")
        count += 1
    input("Press Enter to continue...\n")

def menu(user_id = 'P001'):
    while True:
        choice = input("------------------------------\n"
                       "Enter choose operation\n"
                       "------------------------------\n"
                       "1. Access your medical records\n"
                       "2. View upcoming appointments\n"
                       "3. Update personal information\n"
                       "4. Access billing details and view payment history\n"
                       "5. Log out\n")
        match choice:
            case '1':
                view_medical_records(user_id)
            case '2':
                view_appointments(user_id)
            case '3':
                update_info(user_id)
            case '4':
                view_payment(user_id)
            case '5':
                return
            case _:
                print("Invalid input")

menu()
