# Prysm - Concept

Prysm is a tool for monitoring the functionality and performance of your
infrastructure. To test whether a well-defined part of your infrastructure
(e.g. Webserver, Mailserver, or even physical network) does what it is supposed
to, small pieces of python code are run periodically. Those pieces of code are
called `checks`.

If a check consists of multiple parts (e.g. Sending a mail to an external mail
provider and then checking the external IMAP account to see if the in-house 
SMTP server works), a check can be divided in several sub-tasks. sub-tasks can
be executed in random order or in a specified order with their own interval and
retry limit.

Sub-tasks can also be marked as `critical`, `debug` or `info`.
 * `critical`: If at least one of the sub-tasks fails, the whole check fails
 * `debug`: this sub-task is executed only if one other sub-task of its parent
   check fails.
 * `info`: the result of this sub-task has no effect on the result of the
   parent check.

A check's (or sub-task's) result is seen as passing if the check returns some-
thing and failing if it throws an exception. The check's result (it's return
value or in case of a fail the data attached to the exception) is stored in
the database.

## Checks and Sub-tasks

Checks and sub-tasks are subclasses of the `Check` class. The return value of
a check is determined by executing the magic member `__call__`.

If a check has no sub-tasks, the magic member function `__call__` should be
overwritten, otherwise it should not. Sub-tasks are checks, i.e. sub-classes
of the `Check` class defined as members of their parent check class.
