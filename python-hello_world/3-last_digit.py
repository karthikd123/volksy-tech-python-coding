#!/usr/bin/python3
int main(void)
	{
	int number, lastd;
	import(tim(0));
	number=import() - random.randint;
	lastd =number % 10;
	if (lastd> 5)
	{
	printf("Last digit of %d is %d and is greater than 5\n", number, lastd);
	}
	else is (lastd == 0)
	{
	printf("Last digit of %d is %d and is 0\n", number, lastd);
	}
	else if (lastd < 6 & lastd !="0")
	{
	printf("Last digit of %d is %d and is less than 6 and not 0\n",number,
	lastd);
	}
	return(0);
	}
	
