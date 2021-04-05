# decorators is used to add the extra features in the existing function
#create fun which take argument as function and inner function and inner function can swap value for that function

def division(a,b):
	print(a/b)

def smart_div(func):#take function as argument
	def inner_fun(a,b):# same as division
		if a < b:
			a,b = b,a
		return func(a,b)
	return inner_fun

div = smart_div(division)
div(2,4)

