
info={"key":"value",
      "name":"sarawer",
      "age":23,
      "ID":528,
      "cgpa":3.38,
      "Enroled_cources":["AI","OS","Algo"]}

#in dictionary value can be any data types but keys only can't be list or dict 
#dictionary are unordered and mutable(changeable) and dont allow duplicate keys
print(info)
print(type(info))
print(info["name"])
info["name"]="rahat" #overwrite
print(info["name"])
print(info["Enroled_cources"])


null_dict={}
null_dict["name"]="niloy"
print(null_dict)


#nested dictionary
student={
    "name":"sarawer",
    "subjects":{
        "phy":80,
        "chem":95,
        "math":98
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["math"])

#methodes
print(info.keys()) #return al keys
print(student.keys()) # for nested dict only output outer keys

copy_of_info=list(info.keys()) # typecast dict keys to list
print(copy_of_info)

print(len(info))

print(info.values()) #return al values
print(info.items()) # return al (key,value) pair as touple


print(info.get("name")) # return value of key
print(info.get("name1")) # return none if key not found
# print(info["name1"]) # return error if key not found

info.update({
    "name":"rahat",
    "age":24,
    "ID":529,
    "address":"ECB"
})

print(info)