import json
import re

#================= loads the existing contacts from the file =====================================================================================================
def load_contacts(filename="contacts.json"):
    try:
        with open(filename,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
#================= saves the modifications to the file ===========================================================================================================
def save_contacts(contact_list,filename="contacts.json"):
    with open(filename,'w') as file:
        json.dump(contact_list,file)

#================= contact name is validated =====================================================================================================================
def contact_name_validate(contact_name):
    if not contact_name:
        print("Contact Name can't be empty. Retry.")
        return False
    return True

#================= mobile number is validated =====================================================================================================================
def mob_no_validate(mob_no):
    if mob_no and not re.match(r'^(\+?\d{1,3}[- ]?)?\d{10}$',mob_no):
        print("Invalid Mobile Number. Retry.")
        return False
    return True

#================= landline number is validated =====================================================================================================================
def phone_no_validate(phone_no):
    if phone_no and not re.match(r'^\d{2,5}[- ]?\d{5,8}$',phone_no):
        print("Invalid Landline Number. Retry.")
        return False
    return True

#================= email-id is validated =========================================================================================================================
def email_id_validate(email_id):
    if email_id and not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',email_id,re.IGNORECASE):
        print("Invalid Email-Id. Retry.")
        return False
    return True

#================= adds contact to the contact list ==============================================================================================================
def add_contact(contact_list):
    contact_name = input("Enter name of the contact : ").strip()
    if(not contact_name_validate(contact_name)):
        return
    
    mob_no = input("Enter mobile number (Press Enter if not applicable) : ")
    if(not mob_no_validate(mob_no)):
        return
    
    phone_no = input("Enter landline number (Press Enter if not applicable) : ")
    if(not phone_no_validate(phone_no)):
        return
    
    email_id = input("Enter email-id (Press Enter if not applicable) : ").strip()
    if(not email_id_validate(email_id)):
        return
    
    contact = {
        "name": contact_name,
        "mobile": mob_no if mob_no else "N/A",
        "landline": phone_no if phone_no else "N/A",
        "email": email_id if email_id else "N/A"
    }

    response = input("Do you want to save the contact (Y/N) : ")
    if(response=='Y' or response=='y'):
        print("Contact added successfully to the contact list!")
        contact_list.append(contact)
        save_contacts(contact_list)
    return

#================= searches for a particular contact in contact list =============================================================================================
def search_contact(contact_list):
    contact_name = input("Enter name of the contact to be searched : ").strip().lower()
    for contact in contact_list:
        if contact['name'].lower()==contact_name:
            print("Contact details : ")
            display_contact(contact)
            return
    print("Contact doesn't exist. Add the contact.")
    return

#================= displays particular contact info from contact list =============================================================================================
def display_contact(contact):
    for key,value in contact.items():
        if value!="N/A":
            print(f"{key} : {value}")

#================= updates contact info for particular contact in contact list ====================================================================================
def update_contact(contact_list):
    contact_name = input("Enter name of the contact to be updated : ").strip().lower()
    for contact in contact_list:
        if contact['name'].lower()==contact_name:
            print("Contact details : ")
            display_contact(contact)
            print("Select the option for the fields to be updated :\n1.Contact name\n2.Mobile Number\n3.Phone number\n4.Email Id")
            value = int(input("Field to be updated : "))
            match value:
                case 1:
                    contact_name = input("Enter the new contact name : ").strip()
                    if(not contact_name_validate(contact_name)):
                        return
                    else:
                        contact['name'] = contact_name
                case 2:
                    mob_no = input("Enter the new mobile number : ")
                    if(not mob_no_validate(mob_no)):
                        return
                    else:
                        contact['mobile'] = mob_no
                case 3:
                    phone_no = input("Enter the new phone number : ")
                    if(not phone_no_validate(phone_no)):
                        return
                    else:
                        contact['landline'] = phone_no
                case 4:
                    email_id = input("Enter the new email id : ")
                    if(not email_id_validate(email_id)):
                        return
                    else:
                        contact['email'] = email_id
                case _:
                    print("Invalid.Select the correct option from the list.")
            print("Contact updated successfully!")
            display_contact(contact)
            save_contacts(contact_list)
            return
    print("Contact doesn't exist. Add the contact.")
    return

#================= main function ==================================================================================================================================
def main():
    contact_list = load_contacts()
    loop = True
    while(loop):
        print("=========== Welcome to the Contact Management System ===========\nMenu:\n1.Add the Contact\n2.Search the Contact\n3.Update the Contact\n4.Exit")
        option = int(input("Select the correct option from the above menu to proceed : "))
        match option:
            case 1:
                add_contact(contact_list)
            case 2:
                search_contact(contact_list)
            case 3:
                update_contact(contact_list)
            case 4:
                print("Exiting the program.")
                loop=False
            case _:
                print("Invalid.Select the correct option from the above menu!")
    
main()