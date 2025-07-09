#!/bin/bash
set -euo pipefail

TOOLS_DIR="tools"
PLANTUML_JAR_PATH="$TOOLS_DIR/plantuml.jar"
PLANTUML_DOWNLOAD_URL="https://github.com/plantuml/plantuml/releases/latest/download/plantuml.jar"

if [ ! -f "$PLANTUML_JAR_PATH" ]; then
  echo "Downloading plantuml.jar..."
  mkdir -p "$TOOLS_DIR"
  curl -L -o "$PLANTUML_JAR_PATH" "$PLANTUML_DOWNLOAD_URL"
  echo "plantuml.jar downloaded successfully to $PLANTUML_JAR_PATH"
else
  echo "plantuml.jar already exists in $TOOLS_DIR."
fi
