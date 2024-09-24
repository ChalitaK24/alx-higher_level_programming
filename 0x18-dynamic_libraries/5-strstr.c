#include "main.h"
#include <stddef.h>

/**
 * _strstr - locates a substring
 * @haystack: main string
 * @needle: substring to look for in *haystack
 *
 * Return: pointer if success or NULL
 */

char *_strstr(char *haystack, char *needle)
{
	if (*needle == '\0')
	{
		return (haystack);
	}

	while (*haystack != '\0')
	{
		char *h = haystack;
		char *n = needle;

		while (*h == *n && *n != '\0')
		{
			h++;
			n++;
		}

		if (*n == '\0')
		{
			return (haystack);
		}
		haystack++;
	}
	return (NULL);
}
