# Validation record — 2026-11-02
## Automated checks
- **365 tests passed**, zero failed, zero errors, zero skipped. [JUnit evidence](test-results.xml) records the full run.
- All 65 lab test files plus portal tests were collected. Each lab has three sample contracts, invalid-input rejection, and real form submission; additional cases cover meaningful failure paths.
- The file validator checks 65 project contracts and 195 sample input/output cases. It also parses project Python files and checks for parent-path injection and obvious hardcoded credential formats.
- Dependency compatibility: 74 packages in the clean LangGraph environment passed uv pip check.
- requirements.lock.txt resolved for Python 3.12 across platform markers and includes artifact hashes. Clean installation used --require-hashes.

## Standalone execution
A representative lab was copied outside the repository, then tested in the new environment: **6 tests passed**. The approval lab reopened SQLite checkpoint state and rejected invalid resume behavior. No parent repository source imports were available.

## Browser checks
Chromium exercised the portal search and interview tab and submitted a representative lab form. Desktop (1440px) and mobile (390px) checks passed without horizontal page overflow. Screenshots were visually reviewed, and primary-button contrast/header spacing were refined. All remaining forms have automated AppTest execution; this is not a claim that all 65 layouts were manually audited.

- [Portal desktop](screenshots/portal-desktop.png)
- [Portal mobile](screenshots/portal-mobile.png)
- [Lab desktop](screenshots/lab-desktop.png)
- [Lab mobile](screenshots/lab-mobile.png)

## Local HTTP serving
The A10 loopback server returned the expected Graph response: hello for POST /invoke and rejected an empty request with HTTP 400. This verifies the documented local endpoint, not a managed deployment.

## Verification limits
No paid model request, live LangSmith account write, managed deployment, distributed storage service, production identity provider, cloud alert delivery, or real regional failover was exercised. Optional account paths remain unverified against user accounts. Local fixtures and operational analytics are labeled by their actual scope.

Official documentation hosts were blocked by the environment network policy. APIs were checked using installed signatures/source and executable tests. SDK-internal beta/deprecation warnings remain visible; deprecated query/read application paths were replaced with current v2 examples. Windows/macOS CI is configured but has not run on GitHub yet.

## Publication
The owner created the destination repository after the GitHub API creation route was blocked by environment policy. Publication uses the existing Git connection and is tracked by repository commit history. These checks establish local validation, not managed cloud deployment.
