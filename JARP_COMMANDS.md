# JARP's Command Structure
JARP commands are designed to mimic CLI command structure or syntax. Having said that, there are some slight differences between the two. Here is an example of a JARP command:

> `jarp greetings --hello`

`jarp ` is the prefix of the bot; `greetings` is the Primary Operation, or priop for short; and `--hello` is the First Level Secondary Operation, or FLSO for short.

JARP commands follow a hierarchy, where every command (Primary Operation) has its subcommand(s) (Secondary Operation(s)). Furthermore, each Secondary Operation is split into Levels,
as seen in the example above.

## Primary Operations:
