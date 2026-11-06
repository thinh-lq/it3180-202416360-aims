# Lab 03 -- Bugfix Flow, Conflicts, and Reverting

## 1. What is a merge base?

A **merge base** is the best common ancestor commit of the branches
being merged. Git uses it as the reference point for identifying changes
made independently on each branch. In a typical three-way merge, Git
compares the merge base with each branch tip and combines the resulting
changes. If both branches changed the same lines incompatibly, a merge
conflict may occur.

## 2. Why should `master` and `release/*` use `revert`?

These are shared integration or release branches. Rewriting their
published history can disrupt other contributors and make the repository
difficult to synchronize. `git revert` creates a new commit that applies
the inverse of an earlier commit while preserving the original commit in
history. This keeps the history auditable: both the original change and
its reversal remain visible.

For a merge commit, the mainline parent must be selected, for example:

``` bash
git revert -m 1 <merge_commit_sha>
```
