#pragma once
#include <iostream>
using namespace std;

void testfun(void)
{
	int a = 3;
	int b = 4;
	int c = 5;

	int* ptr1 = &a;
	cout << "ptr1 = " << *ptr1 << endl;
	int* ptr2 = ptr1;
	cout << "ptr2 = " << *ptr2 << endl;
	ptr1 = &b;
	cout << "ptr1 = " << *ptr1 << endl;
	cout << "ptr2 = " << *ptr2 << endl;
}

