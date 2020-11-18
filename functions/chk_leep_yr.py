def chk_leap_year(yr):
	result = "Leap Year.." if yr % 400 == 0 else "Leap Year.." if yr % 4 == 0 and yr % 100 != 0 else "Non Leap Year"
	print(result)

yr = int(input("Enter Year :"))
chk_leap_year(yr)