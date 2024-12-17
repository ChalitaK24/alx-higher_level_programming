#!/usr/bin/node

// Prints My number: <first argument converted in integer>
// If the first argument can be converted to an integer

const args = process.argv.slice(2);

const fstArg = parseInt(args[0]);

if (!isNaN(fstArg))
{
	console.log(`My nnumber: ${fstArg}`);
}
else
{
	console.log("Not a number");

