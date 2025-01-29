import csv

# Registers a new donor with their details in the CSV file.
def register_donor(donor_name, donor_age, blood_type, blood_volume, phone):
    with open('blood_records.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([donor_name, donor_age, blood_type, blood_volume, phone])
    print('Donor Successfully Registered!')

# Increases the blood volume for a specific donor.
def increment_blood(donor_name, volume_to_add):
    with open('blood_records.csv', 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        all_rows = list(csv_data)  # Retrieve all rows.
    with open('blood_records.csv', 'w', newline='\n') as csv_file:
        csv_writer = csv.writer(csv_file)
        for record in all_rows:
            if record[0] == donor_name:  # Locate donor by name.
                record[1] = str(int(record[1]) + volume_to_add)  # Update the blood volume.
            csv_writer.writerow(record)
    print('Blood Volume Updated!')

# Deletes a donor's details based on their name.
def delete_donor(donor_name):
    with open('blood_records.csv', 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        rows_in_file = list(csv_data)  # Store all rows.
    with open('blood_records.csv', 'w', newline='\n') as csv_file:
        csv_writer = csv.writer(csv_file)
        for entry in rows_in_file:
            if entry[0] != donor_name:  # Skip the donor to remove.
                csv_writer.writerow(entry)
    print('Donor Details Removed!')

# Lists all registered donors along with their blood group and volume.
def list_donors():
    with open('blood_records.csv', 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        for donor in csv_data:
            print(donor[0], " : ", donor[1], ",", donor[3], " : ", donor[2])

# Searches for donors who belong to a specific blood group.
def find_donors_by_group(blood_type):
    with open('blood_records.csv', 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        donor_found = False
        for record in csv_data:
            if record[2] == blood_type:  # Match blood group.
                print(record[0], " : ", record[1], ",", record[3], " : ", record[2])
                donor_found = True
        if not donor_found:
            print('No donors with the specified blood group were found.')

# Deducts the specified blood amount from the stock of a particular group.
def deduct_blood(blood_type, volume_to_use):
    with open('blood_records.csv', 'r') as csv_file:
        csv_data = csv.reader(csv_file)
        donor_records = list(csv_data)  # Collect all records.
    with open('blood_records.csv', 'w', newline='\n') as csv_file:
        csv_writer = csv.writer(csv_file)
        for entry in donor_records:
            if entry[2] == blood_type:  # Match the blood group.
                if int(entry[1]) >= volume_to_use:  # Ensure enough blood is available.
                    entry[1] = str(int(entry[1]) - volume_to_use)  # Deduct the volume.
                    csv_writer.writerow(entry)
                else:
                    print('Insufficient blood available!')
            else:
                csv_writer.writerow(entry)
    print('Blood Deducted Successfully!')

# Main loop to handle user choices.
while True:
    print("\n--- Blood Bank Management System ---")
    print("1. Register New Donor")
    print("2. Delete Donor Details")
    print("3. Display All Donors")
    print("4. Search Donors by Blood Group")
    print("5. Deduct Blood")
    print("6. Add Blood to Donor")
    print("7. Exit Program")

    user_choice = input(">>>: ")
    if user_choice == "1":
        # Collect donor details for registration.
        donor_name = input("Enter donor's name: ")
        donor_age = int(input("Enter donor's age: "))
        if donor_age < 18:  # Validate age.
            print('Age must be at least 18 to register!')
            continue
        phone = input("Enter phone number: ")
        if len(phone) != 10:
            print('Invalid phone number entered!')
            continue

        # Select the blood group.
        blood_group_option = int(input("Select blood group:\n1. A+\n2. A-\n3. B+\n4. B-,\n5. AB+\n6. AB-\n7. O+\n8. O-\n>>> "))
        blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
        if 1 <= blood_group_option <= 8:
            blood_type = blood_groups[blood_group_option - 1]
        else:
            print('Invalid selection!')
            continue
        blood_volume = int(input("Enter initial blood amount: "))
        register_donor(donor_name, donor_age, blood_type, blood_volume, phone)
    elif user_choice == "2":
        donor_name = input("Enter the name of the donor to delete: ")
        delete_donor(donor_name)
    elif user_choice == "3":
        list_donors()
    elif user_choice == "4":
        blood_group_option = int(input("Select blood group:\n1. A+\n2. A-\n3. B+\n4. B-,\n5. AB+\n6. AB-\n7. O+\n8. O-\n>>> "))
        if 1 <= blood_group_option <= 8:
            blood_type = blood_groups[blood_group_option - 1]
        else:
            print('Invalid choice!')
            continue
        find_donors_by_group(blood_type)
    elif user_choice == "5":
        blood_group_option = int(input("Select blood group:\n1. A+\n2. A-\n3. B+\n4. B-,\n5. AB+\n6. AB-\n7. O+\n8. O-\n>>> "))
        if 1 <= blood_group_option <= 8:
            blood_type = blood_groups[blood_group_option - 1]
        else:
            print('Invalid choice!')
            continue
        volume_to_use = int(input("Enter blood volume to deduct: "))
        deduct_blood(blood_type, volume_to_use)
    elif user_choice == "6":
        donor_name = input("Enter the name of the donor to add blood to: ")
        volume_to_add = int(input("Enter amount of blood to add: "))
        increment_blood(donor_name, volume_to_add)
    elif user_choice == "7":
        print("Exiting the system. Thank you for using the Blood Bank Management System!")
        break
    else:
        print("Invalid option. Please try again.")
