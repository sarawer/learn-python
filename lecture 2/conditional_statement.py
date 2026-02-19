"""
if(condition):
    statement1
elif(condition):
    statement2
else:
    statementN
"""

light=input()

if(light=="green"):
    print("GO")
elif(light=="red"):
    print("STOP")
elif(light=="yellow"):
    print("WAIT")
else:
    print("ERROR")