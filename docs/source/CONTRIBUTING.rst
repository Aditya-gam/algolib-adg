.. Copyright (C) 2023, Aditya G.

Contributor Workflow
====================

#.  Copy :code:`specs/template.yml` → :code:`specs/MyAlgo.yml` and fill in fields.
#.  Run :code:`pre-commit run --all-files` (validates YAML schema).
#.  Commit and push – the bot creates code/tests/docs and opens a PR.
#.  Review generated PR; merge when checks are green.
