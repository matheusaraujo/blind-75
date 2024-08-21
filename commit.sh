#!/bin/bash

RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
RESET=$(tput sgr0)

TOPICS=(
  "arrays-hashing"
  "two-pointers"
  "sliding-window"
  "stack"
  "binary-search"
  "linked-list"
  "trees"
  "heap"
  "backtracking"
  "tries"
  "graphs"
  "advanced-graphs"
  "1d-dynamic-programming"
  "2d-dynamic-programming"
  "greedy"
  "intervals"
  "math-geometry"
  "bit-manipulation"
)

is_valid_topic() {
  local topic=$1
  for valid_topic in "${TOPICS[@]}"; do
    if [ "$topic" == "$valid_topic" ]; then
      return 0
    fi
  done
  return 1
}

get_new_files() {
  git status --short | grep -E '\.py$' | awk '{print $2}' | sed '/^$/d'
}

validate_file_count() {
  local file_count
  file_count=$(echo "$1" | wc -l | tr -d ' ')
  if [ "$file_count" -ne 1 ]; then
    printf "%sinvalid git status%s\n" "$RED" "$RESET"
    exit 1
  fi
}

build_commit_message() {
  local topic=$1
  local file_name=$2

  if [[ "$file_name" == extras/* ]]; then
    echo "feat($topic): $(basename "$file_name") [extras]"
  else
    echo "feat($topic): $(basename "$file_name")"
  fi
}

main() {
  if [ "$#" -ne 1 ]; then
    printf "%susage: %s %s\n" "$RED" "$0" "$RESET"
    exit 1
  fi

  local topic="$1"

  if ! is_valid_topic "$topic"; then
    printf "%sinvalid topic%s\n" "$RED" "$RESET"
    exit 1
  fi

  local new_files
  local file_name
  local commit_message

  new_files=$(get_new_files)
  validate_file_count "$new_files"

  file_name=$(echo "$new_files" | head -n 1)
  commit_message=$(build_commit_message "$topic" "$file_name")

  git add "$file_name"
  git commit -m "$commit_message"

  printf "%scommitted%s\n" "$GREEN" "$RESET"
}

main "$@"
