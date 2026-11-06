# Lab 05 -- Hotfix Flow and Multi-Version Maintenance

## 1. Why not merge the entire hotfix branch into `master`?

The hotfix branch is based on `release/lab04`, where the version is
`1.0.0`. The hotfix preparation may update version metadata to `1.0.1`,
while `master` may already contain the newer `1.1.0` development
version. Merging the whole branch can therefore introduce unrelated or
conflicting release metadata and changes from the older release line.

The lab transfers only the actual bug-fix commit to `master` by using
`git cherry-pick -x <FIX_SHA>`. The `-x` option adds a reference to the
source commit, preserving traceability.

## 2. Why was the `v1.1.0` tag not created in Part A?

The hotfix must first be propagated and merged into `release/lab05`.
Creating the `v1.1.0` tag too early would permanently identify a commit
that does not yet contain the required fix. The tag should be created
only after the fix is integrated and the release state is ready.

A published tag should not be moved. If `v1.1.0` had already been
created at the earlier commit, the corrected release would need a new
patch version, `v1.1.1`.

## 3. What are the advantages and disadvantages of upstream-first compared with release-first?

**Upstream-first** applies the fix to the main development line first
and then propagates it to affected release branches.

-   **Advantages:** The mainline receives the correction early; there is
    a clear source commit for later cherry-picks; the fix is less likely
    to be absent from future development.
-   **Disadvantages:** The fix must still be propagated deliberately to
    every maintained release line. Missing a propagation can leave an
    older supported version with the bug.

**Release-first** fixes the affected release branch first, then
propagates the fix upstream.

-   **Advantages:** It prioritizes the version that needs urgent
    maintenance and fits the course Release Flow used in this exercise.
-   **Disadvantages:** The fix must still be propagated to `master`;
    otherwise, the bug may reappear in later development.

The course comparison identifies the course Release Flow as
release-first and the Microsoft-style Release Flow as upstream-first.

## 4. If the fix is not propagated to `release/lab05`, which command from Part F can detect it?

Part F uses `git cherry` to compare patch-equivalent commits between
branches. Its example is:

``` bash
git cherry -v origin/master origin/release/lab04
```

For the `release/lab05` line, apply the same comparison pattern with
that branch:

``` bash
git cherry -v origin/master origin/release/lab05
```

`git cherry` compares the commits reachable from the second branch with
the first branch, using patch equivalence rather than requiring
identical commit IDs. A `+` indicates a commit whose equivalent patch is
not found in the first branch; a `-` indicates that an equivalent patch
is already present there. Therefore, inspect the output for the hotfix
commit and verify that the fix has reached the intended release line.
The exact comparison direction matters.

## 5. Why use `cherry-pick -x` when propagating a hotfix?

`cherry-pick` applies the changes introduced by a selected commit onto
the current branch without merging the entire source branch. This is
useful when release lines have diverged and only one correction should
be transferred. The `-x` option records the original commit SHA in the
new commit message, making the copied fix traceable to its source.

## 6. What does it mean to maintain multiple release versions in parallel?

More than one released version remains supported at the same time. A bug
fix may need to be applied independently to several release branches,
while `master` continues to receive new features. Configuration auditing
verifies that each affected version contains the required fix, passes
its tests, and has release metadata consistent with its source code.
