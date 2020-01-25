Description
------------------------------------------------------------------------------

Ansible role to apply user wide configuration.

This role performs the following actions:

- Ensure the requirements are installed.

- Ensure the current user can obtain administrative (root) permissions.

- Update the apt cache.

- Ensure dependencies are installed.

- If the **user_skeleton** variable is defined and the **users** variable is
  defined, clone the git repositories listed into each user home folder.

- If the **configuration** variable is defined and the **users** variable is
  defined, clone the git repositories listed on it into each user home folder.

This role do not expand files or URLs by default because the most common case
is to specify URLs that points directly to a skeleton repository, so the
default behaviour for this role is to treat file paths and URLs as plain text.

You can change the default behaviour by:

- Setting the **expand** variable to *true*.

Or

- Add to an item the attribute **item_expand** setted to *true*.
