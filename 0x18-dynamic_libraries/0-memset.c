#include "main.h"

/**
 * _memset - fills memeory with const char byte
 * @s: pointer to a &s
 * @b: constant byte
 * @n: number of bytes
 *
 * Return: s
 */

char *_memset(char *s, char b, unsigned int n)
{
	char *a = s;
	unsigned int i;

	for (i = 0; i < n; i++)
	{
		*a = b;
		a++;
	}
	return (s);
}
