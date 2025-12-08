# Joodeh's Archive Robot Personnel (JARP)
JARP is the personal discord bot for Joodeh's Archive discord server. JARP's initial purpose was to manage and save links to websites and videos 
or any other media found on the internet or created by fellow JA members, as well as be able to recall the link or media when prompted by a user;
however, we aim to implement other operations be it for convienence, automation or entertainment.

This is a personal project of mine. Through it, I hope to improve my understanding of Python and Github and to hone my skills in documenting and writing better and clearer code :3



## JARP's Command Structure
JARP commands are designed to mimic CLI command structure or syntax. Having said that, the JARP command structure and the commands themselves are not a hundred percent based on CLI. Here is an example of a JARP command:

> `jarp greetings --hello`

`jarp ` is the prefix of the bot; `greetings` is the Primary Operation, or PO (priop) for short; and `--hello` is the First Level Secondary Operation, or FLSO for short.

JARP commands follow a hierarchy, where every command (Primary Operation) has its subcommand(s) (Secondary Operation(s)). Furthermore, each Secondary Operation is split into Levels,
as seen in the example above.

### Primary Operations:
The Primary Operations are the main commands which the user will want to be executed. Take, for example, the Primary Operation `role`. Any set of actions the user wishes to perform
with the parent operation `role` will be a child operation, that is the Secondary Operation, of it, thus maintaining coherency. For example, if a user wishes to create a role, they would need to enter the following:

> `jarp role --create-role <arguments>`

### Secondary Operations:
Now, some commands require only a Primary Operation to execute. Say, a ping command. Specifically, there are commands that do not require any additional options or arguments.
Furthermore, there are commands that require multiple options or arguments. For our previous example, the Primary Operation `role` has a Secondary Operation `--create-role`, and that Secondary Operation would require further information or arguments for the command to be executed.

As such, we find a need for a lower level of Secondary Operations. I don't see a reason for there being more than two levels of depth, but perhaps if JARP ever grows in complexity (which I doubt it will; no disrespect to our beloved JARP) I'll add more levels. For now, let's consider only the two levels:

**First Level Secondary Operation (FLSO) and Second Level Secondary Operations (SLSO):**

These Secondary Operations are the main subcommands. They are the direct children of the Primary Operation. That is to say they're the set of actions the user wants to perform with the Primary Operation.
Some Secondary Operations or subcommands do not require any more options or arguments, thus ending the hierarchy. However, others require further information, as does the Secondary Operation `--create-role`.
Any additional Secondary Operations will be classified as the Second Level Secondary Operation(s). For example, say the SLSOs for the FLSO `--create-role` would be `--name` and `--colour`, each of which will take an argument. Thus, the final command will look like this:

> `jarp role --create-role --name "jarp" colour #123123`

**The Desired Hierarchy:**
JARP_COMMAND_STRUCTURE
jarp (JARP's Prefix) --> role (Primary Operation) --> --create-role (FLSO) --> --name (SLSO) <argument> --colour (SLSO) <argument>




