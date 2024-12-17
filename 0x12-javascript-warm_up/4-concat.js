#!/usr/bin/node

// prints two arguments passed to it, in the following format: “ is ”

const args = process.argv.slice(2);

const fstArg = args[0] || "undefined";
const scdArg = args[1] || "undefined";

console.log(`${fstArg} is ${scdArg}`);
