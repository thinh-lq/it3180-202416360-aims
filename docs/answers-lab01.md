# Lab 01 -- Environment Setup and Refactor Flow

## 1. Why use `git mv`?

`git mv` moves or renames a file and stages the change in one command.
It makes the intended file operation explicit and convenient to review.
Git does not store a special rename operation; it detects renames by
comparing file contents. Therefore, manually moving a file and then
staging the deletion and addition can produce the same result.

## 2. Is `release/lab01` a baseline?

Yes. In this lab, `release/lab01` records the completed state submitted
for Lab 01. A **baseline** is an identified configuration that serves as
a reference for comparison, auditing, and later reconstruction. The
branch provides a stable reference point for the work completed in that
lab.

## 3. Why not commit directly to `master`, even when working alone?

Using a separate branch and integrating through a Pull Request keeps the
main development line controlled. A PR provides an opportunity to
inspect the diff, review tests, document the purpose of the change, and
preserve a consistent workflow. This remains useful for a solo developer
because it reduces accidental changes to `master` and creates an
auditable history.
