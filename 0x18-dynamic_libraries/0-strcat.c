#include "main.h"

/**
 * _strcat -links together two stings
 * @src: string appended from
 * @dest: string appended to
 *
 * Return: string
 */

char *_strcat(char *dest, char *src)
{
	char *lnk = dest;

	while (*dest != '\0')
	{
		dest++;
	}

	while (*src != '\0')
	{
		*dest = *src;
		dest++;
		src++;
	}

	*dest = '\0';

	return (lnk);
}
