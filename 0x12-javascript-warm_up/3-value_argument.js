#!/usr/bin/node

// Prints the first argument passed to it

const args = process.argv.slice(2);

const fstArg = args[0] || "No argument";

conosle.log(fstArg);
