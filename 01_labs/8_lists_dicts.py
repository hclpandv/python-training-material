# List is a python datatype equivalent to array in other languages.
# List conatins collection of one or multiple datatypes. 
# Unlike array which contains similar type of datatypes

#-------------------
#----------- List
#-------------------

my_server_list = ["vm00001234", "vm00002534", "vm00004567", "vm00006969"]
for item in my_server_list:
    print("Server Name: " + item)

print("Total Servers: " + str(len(my_server_list)))

# Add item(s)
my_server_list.append("vm10001234")
print(my_server_list)

my_server_list.extend("vm20001234") # Try ["vm20001234"] 
print(my_server_list)

my_server_list.insert(2, "vm20001234")
print(my_server_list)

# Remove item(s)
del my_server_list[0]
print(my_server_list)

my_server_list.pop() #try pop(2)
print(my_server_list)

# List may contain another List as its element
# List may contain another List as its element

my_config_list = ["vm00001234", 
                  "vm00002534", 
                  "vm00004567", 
                  "vm00006969", 
                  ["Linux", "Windows", "Mac"], 
                  ["192.169.0.1", "192.169.0.2", "192.169.0.3"]
                 ]  # Notice the whitespace formatting

print(my_config_list)
print(my_config_list[4])
print(my_config_list[5][1])

#-------------------
#----------- Tuple
#-------------------

# Tuple is a read-only List. Its Immutable, you cant add, remove or change any itme in the list

my_server_tuple = ("vm00001234", "vm00002534", "vm00004567", "vm00006969")
print(my_server_tuple)

#-------------------
#------- Dictionary
#-------------------

# Dictionary is a comma seperated list of key value pairs.
# Dictionary data is not indexed hence you have to access an iten with its reference key or value

my_vm_config = {"hostname": "vm00002314", "mgmt_ip": "192.169.3.12", "domain": "vikiscripts.github.io" }
print(my_vm_config)
print(my_vm_config["mgmt_ip"])


my_vm_config = {
                "hostname" : "vm00002314",
                "pvt_ip" : "10.48.3.12", 
                "domain": "vikiscripts.github.io",
                "network_config": {
                                    "mgmt_ip": "192.169.3.12",
                                    "vnet": "vnet1",
                                    "nic" : 2
                                  }
                }
print(my_vm_config["network_config"]["vnet"])




