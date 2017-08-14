#ADVANCED TOPICS IN PYTHON
#List Slicing
##########################
#1.The string in the editor is garbled in two ways:

#Our message is backwards.
#The letter we want is every other letter.
#Use list slicing to extract the message and save it to a variable called message.

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-1]
message = message[0:len(message):2]