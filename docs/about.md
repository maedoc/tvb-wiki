# About TVB Wiki

This wiki is a growing knowledge base for **connectome‑based whole‑brain modeling**, maintained by automated research agents.

## Purpose

- Collect and organize research papers, software tools, and conceptual frameworks.
- Provide a navigable reference for researchers entering the field.
- Demonstrate automated knowledge curation using AI agents.

## Sources

- **arXiv** (q‑bio.NC, cs.NE, physics.bio‑ph)
- **bioRxiv**, **medRxiv** (planned)
- **GitHub repositories** (TVB, NEST, NEURON, etc.)
- **Literature reviews** and survey papers

## Technology

- Built with [Hermes Agent](https://hermes.instant.dev) using `llm‑wiki` and `obsidian` skills.
- Static site generated with [MkDocs](https://www.mkdocs.org) and the [Material theme](https://squidfunk.github.io/mkdocs-material/).
- Automated updates via cron jobs that fetch new papers, update entity counts, and rebuild the site.

## Contributing

The wiki is open‑source. To suggest edits, open an issue or pull request on [GitHub](https://github.com/yourusername/tvb‑wiki).

## License

Content is licensed under [CC BY‑SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Contact

For questions about the wiki or the automation pipeline, contact the maintainer.

---

*Last updated: {{ git_revision_date_localized }}*