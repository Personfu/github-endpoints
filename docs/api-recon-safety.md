# GitHub API Recon Safety Notes

GitHub endpoint research is useful for developer education, automation, and repo hygiene. It must stay inside authenticated account scope, public API documentation, and rate-limit-respecting workflows.

## Allowed

- Catalog public REST/GraphQL endpoints.
- Build scripts that inspect your own repositories.
- Generate repo health reports.
- Validate branch, issue, PR, and workflow metadata.
- Respect rate limits and token permissions.

## Blocked

- Token harvesting.
- Secret scanning outside authorized repos.
- Abuse of search APIs for credential discovery.
- Scraping private data.
- Bypassing rate limits.
- Automating spam issues, PRs, stars, follows, or reactions.

## FLLC use cases

- Achievement-aware but non-spammy contribution planning.
- Repo README/security/contributing coverage reports.
- GitHub Pages visual health checks.
- Release and deployment evidence collection.
- Internal automation dashboards.
