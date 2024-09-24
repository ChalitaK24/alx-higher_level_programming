#include "main.h"
#include <stddef.h>

/**
 * _strchr - locates first occurace of character 'c' string
 * @s: string
 * @c: character
 *
 * Return: NULL
 */

char *_strchr(char *s, char c)
{
	int i = 0;

	while (s[i] != '\0')
	{
		if (s[i] == c)
		{
			return (&s[i]);
		}
		i++;
	}
	if (s[i] == c)
	{
		return (&s[i]);
	}

	return (NULL);
}
