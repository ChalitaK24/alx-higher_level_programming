#include "main.h"

/**
 * _abs - prints absolte value of an integer
 * @n: variable
 *
 * Return: 0
 */

int _abs(int n)
{
	if (n < 0)
		return (n * -1);
	else
		return (n);
	return (0);
}
