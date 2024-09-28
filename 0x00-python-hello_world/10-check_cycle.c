#include "lists.h"

/**
 * check_cycle - checks singly linked list has a cycle 
 * @list: ptr to head
 *
 * Return: 0 no cycle, 1 cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *onenode = list;
	listint_t *twonode = list;

	if (list == NULL)
	{
		return (0);
	}

	while (twonode != NULL && twonode->next != NULL)
	{
		onenode = onenode->next;
		twonode = twonode->next->next;

		if (onenode == twonode)
		{
			return (1);
		}
	}

	return (0);
}
