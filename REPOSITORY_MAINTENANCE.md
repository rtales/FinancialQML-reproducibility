# Repository maintenance

The project is maintained as two separate repositories:

1. **Private development repository** — the working source of truth for ongoing research and development.
2. **Public reproducibility repository** — a clean release of the code, frozen data, manuscript source, and documentation needed to reproduce the reported analysis.

## Updating the public release

For each update, prepare the change in the private repository, rerun the input checks, tests, and full reproduction, and review all changed files for accuracy, licensing, and consistency with the manuscript. Then copy only the reviewed release artifacts into the public repository, update its version and checksums, rerun the public CI workflow, and publish a tagged release. Keep the public repository's history independent: do not push the private repository's development history or internal working records into it.

When an update changes the manuscript or frozen data, create a corresponding versioned archive and update the article's repository and archive citations to identify the released version. Preserve earlier public release tags so published results remain traceable to their exact inputs.
