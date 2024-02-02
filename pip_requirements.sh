#!/bin/bash

if [ "$#" -eq 0 ]; then
  echo $'\nProvide at least one Python package name\n'
else
  dev=false
  packages=()

  # Check for --dev flag
  for arg in "$@"; do
    if [ "$arg" = "--dev" ]; then
      dev=true
    else
      packages+=("$arg")
    fi
  done

  # Install packages and update requirements files
  for package in "${packages[@]}"; do
    pip install "$package"
    if [ "$dev" = true ]; then
      pip freeze | grep -i "$package" >> requirements-dev.txt
    else
      pip freeze | grep -i "$package" >> requirements.txt
    fi
  done
fi
