#include "main.h"

/**
 * _puts - prints charcter string
 * @str: character string pointer
 *
 * Return: void
 */



void _puts(char *str)
{

	while (*str)
	{
		_putchar(*str);
		str++;
	}
	_putchar('\n');
}
