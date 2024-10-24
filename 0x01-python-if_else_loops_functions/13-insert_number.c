#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insetrs number into a sorted list
 * @head: pointer to head of list
 * @number: number to insert
 *
 * Return: the address of the new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *c_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	
	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	c_node = *head;

	while (c_node->next != NULL && c_node->next->n < number)
	{
		c_node = c_node->next;
	}

	new_node->next = c_node->next;
	c_node->next = new_node;

	return (new_node);
}
