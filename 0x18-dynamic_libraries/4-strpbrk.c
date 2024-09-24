#include "main.h"
#include <stddef.h>

/**
 * _strpbrk - locates first occurance of any
 * bytes of string 'accept' in string 's'
 * @s: string to be checked
 * @accept: source string to check for
 *
 * Return: pointer if success or NULL
 *
 */

char *_strpbrk(char *s, char *accept)
{
	int i;
	int j;


	for (i = 0; s[i] != '\0'; i++)
	{
		for (j = 0; accept[j] != '\0'; j++)
		{
			if (s[i] == accept[j])
			{
				return (&s[i]);
			}
		}
	}
	return (NULL);
}
