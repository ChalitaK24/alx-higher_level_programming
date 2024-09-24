#include "main.h"
#include <string.h>


/**
 * _strspn - gets the lenght of a prefix substring
 * @s: initial part of the string
 * @accept: characters to be checked in s
 *
 * Return: n
 */

unsigned int _strspn(char *s, char *accept)
{
	unsigned int n = 0;
	int i;
	int j;
	int sget;

	int s_len = strlen(s);
	int accept_len = strlen(accept);

	for (i = 0; i < s_len; i++)
	{
		sget = 0;

		for (j = 0; j < accept_len; j++)
		{
			if (s[i] == accept[j])
			{
				sget = 1;
				break;
			}
		}

		if (sget)
		{
			n++;
		}
		else
		{
			break;
		}
	}

	return (n);
}
