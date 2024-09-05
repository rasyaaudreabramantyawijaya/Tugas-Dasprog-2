def check_service(service_type, miles):
    if service_type == 1:
        
        if 1500 < miles <= 3000:
            return "Vehicle must be serviced."
        else:
            return "Vehicle does not need servicing for First Service."
    elif service_type == 2:
        
        if 3001 < miles <= 4500:
            return "Vehicle must be serviced."
        else:
            return "Vehicle does not need servicing for Second Service."
    else:
        return "Invalid service selection."

print("(1) First Free Service")
print("(2) Second Free Service")
service_type = int(input("Enter the Free Service number>> "))
miles = int(input("Enter number of Miles>> "))

message = check_service(service_type, miles)
print(message)