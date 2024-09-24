#include "main.h"

/**
 * _strncpy - copy most of the string
 * @dest: string destination
 * @src: string source
 * @n: number of char to cpy
 *
 * Return: cpd
 */

char *_strncpy(char *dest, char *src, int n)
{
	char *cpd = dest;

	while (*src != '\0' && n > 0)
	{
		*dest = *src;
		dest++;
		src++;
		n--;
	}

	while (n > 0)
	{
		*dest = '\0';
		dest++;
		n--;
	}

	return (cpd);
}
