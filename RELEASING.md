# Releasing

A release is a git tag `X.Y.Z` on `main`. Pushing the tag runs
`.github/workflows/release.yml`, which builds the package, creates the GitHub
release and publishes to PyPI. The GitHub release body is the CHANGELOG section
of that version (`.github/scripts/release_notes.sh`); the workflow fails before
publishing anything if the section is missing or empty. PyPI has no per-release
notes, so its project page links to the CHANGELOG instead.

The tag, the `pyproject.toml` version and the CHANGELOG must all name the same
version. The workflow fails before building if the tag differs from the
`pyproject.toml` version, or if the CHANGELOG has no notes for it.

Versions follow [semantic versioning](https://semver.org/): a breaking change
(see the **Breaking** entries in the CHANGELOG) needs a new major version.

1. Make sure `main` is green and `pytest -m live` passes with a real key
   (`DELIJN_API_KEY=... uv run pytest -m live`).
2. In a branch `chore/release-X.Y.Z`:
   - Rename `## [Unreleased]` in `CHANGELOG.md` to `## [X.Y.Z] - YYYY-MM-DD`,
     add a fresh empty `## [Unreleased]` above it, and update the link
     definitions at the bottom (`[Unreleased]` compares `X.Y.Z...main`, plus a
     new `[X.Y.Z]` release link).
   - Set `version = "X.Y.Z"` in `pyproject.toml`.
   - Run `uv lock`; the lock file records the project version and CI runs
     `uv lock --check`.
3. Open a PR, wait for CI, squash-merge it.
4. Tag the merge commit and push the tag:

   ```sh
   git switch main && git pull
   git tag X.Y.Z
   git push origin X.Y.Z
   ```

5. Check the Release workflow run, the GitHub release and
   <https://pypi.org/project/lijnpy/>. A version cannot be re-uploaded to PyPI,
   so fix mistakes with a new patch version.
