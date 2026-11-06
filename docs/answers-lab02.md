# Lab 02 -- Feature/Topic Flow and Pull Requests

## 1. Why synchronize `master` before opening a Pull Request?

The target branch may have changed while the feature branch was being
developed. Synchronizing with the latest `master` exposes integration
problems earlier, allows conflicts to be resolved before review, and
makes it possible to test the feature against the current codebase. This
reduces the risk of discovering incompatibilities only at merge time.

## 2. When should a branch not be rebased?

A branch should generally not be rebased after its commits have been
shared with other developers or used as the basis for their work. Rebase
rewrites commits and gives the rewritten commits new SHA identifiers.
Other developers may still have histories based on the old commits,
causing divergence and difficult synchronization. The practical rule is
to rebase only commits that have not been shared.

## 3. How are `feature/*` and `topic/*` different?

Both are working branches created from `master` and normally integrated
back into `master` through a Pull Request. A `feature/*` branch
represents a product capability or user-facing feature, such as
`feature/discount`. A `topic/*` branch represents a focused work topic
or preparatory task, such as `topic/prepare-release-1.0.0`. The
distinction is mainly the purpose and scope expressed by the branch
name.
