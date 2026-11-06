# Lab 04 -- Release Flow and Versioning

## 1. Why should `release/*` not be merged back into `master`? How does this compare with GitFlow?

In the course Release Flow, `master` remains the main development line,
while `release/*` is a maintenance line for a submitted version. The
release branch is created from `master` and can receive version-specific
fixes without making the older release line the source of new
development. Merging the release branch back into `master` is not part
of the prescribed course flow.

GitFlow uses a different branch model: `main` (or `master`) stores
production releases and `develop` is the integration branch. Release and
hotfix branches are integrated according to that model. The two
workflows should not be treated as identical.

## 2. Why is the release version `1.0.0` rather than `0.4.0`?

The course treats the completion of the first stable, full release as
version `1.0.0`. Under Semantic Versioning, `0.y.z` denotes an initial
development stage in which the public interface is not yet considered
stable. The earlier lab baselines are labeled `0.1.0`, `0.2.0`, and
`0.3.0` as course milestones, while the completed stable release is
designated `1.0.0`. Version numbering reflects release maturity and
compatibility expectations, not simply the number of labs completed.

## 3. Why prepare the `1.0.0` release on `master` first instead of making the preparation changes directly on `release/lab04`?

The release branch should be created from a prepared and reviewed
`master` state. Preparing the version number, release notes, and
`CHANGELOG` on `master` ensures that the release baseline is derived
from the main development history. After those changes are merged,
`release/lab04` can be created from that exact state and used to freeze
the submitted version. This separates release preparation from
maintenance of an established release line.
