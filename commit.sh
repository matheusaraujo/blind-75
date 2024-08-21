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

if [ "$#" -ne 1 ]; then
  printf "%susage: %s %s\n" "$RED" "$0" "$RESET"
  exit 1
fi

TOPIC="$1"

if ! is_valid_topic "$TOPIC"; then
  printf "%sinvalid topic%s\n" "$RED" "$RESET"
  exit 1
fi

NEW_FILES=$(git status --short | grep -E '\.py$' | awk '{print $2}' | sed '/^$/d')
FILE_COUNT=$(echo "$NEW_FILES" | sed '/^$/d' | wc -l | tr -d ' ')

if [ "$FILE_COUNT" -ne 1 ]; then
  printf "%sinvalid git status%s\n" "$RED" "$RESET"
  exit 1
fi

FILE_NAME=$(echo "$NEW_FILES" | head -n 1)

if [[ "$FILE_NAME" == extras/* ]]; then
  COMMIT_MESSAGE="feat($TOPIC): $(basename "$FILE_NAME")  [extras]"
else
  COMMIT_MESSAGE="feat($TOPIC): $(basename "$FILE_NAME")"
fi

git add "$FILE_NAME"
git commit -m "$COMMIT_MESSAGE"

printf "%scommitted%s\n" "$GREEN" "$RESET"
