#include "main.h"

/**
 * _strcpy - copies one string to another
 * @dest: copied string
 * @src: original string
 *
 * Return: dest
 */

char *_strcpy(char *dest, char *src)
{
	char *cpptr = dest;
	char *optr = src;

	while (*optr != '\0')
	{
		*cpptr = *optr;
		cpptr++;
		optr++;
	}

	*cpptr = '\0';

	return (dest);
}
