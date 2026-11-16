#!/usr/bin/env bash
# Print the CHANGELOG section of one version, without its heading.
# Usage: .github/scripts/release_notes.sh 2.0.0 [CHANGELOG.md]
# Exits with an error when the version has no section or the section is empty,
# so a release without notes fails instead of publishing an empty release.
set -euo pipefail

version="${1:?usage: release_notes.sh VERSION [CHANGELOG]}"
changelog="${2:-CHANGELOG.md}"

notes="$(awk -v heading="## [${version}]" '
  index($0, heading) == 1 { found = 1; next }
  found && /^## \[/ { exit }
  found && /^\[[^]]+\]: / { exit }
  found { print }
' "$changelog")"

# Trim leading and trailing blank lines
notes="$(printf '%s\n' "$notes" | sed -e '/./,$!d' | sed -e ':a' -e '/^\n*$/{$d;N;ba' -e '}')"

if [[ -z "${notes//[[:space:]]/}" ]]; then
  echo "No CHANGELOG notes found for ${version} in ${changelog}" >&2
  exit 1
fi
printf '%s\n' "$notes"
