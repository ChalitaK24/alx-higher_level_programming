#include "main.h"

/**
 * _strlen - prints length of a string
 * @s: pointer
 *
 * Return: 0
 */

int _strlen(char *s)
{
	int ln = 0;

	while (s[ln] != '\0')
	{
		ln++;
	}
	return (ln);
}
