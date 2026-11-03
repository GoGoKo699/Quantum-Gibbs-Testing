# Hosted mathematics checks

These read-only helpers compare the mathematical expressions in a pinned source commit with their actual GitHub MathML at wide and narrow viewports. They save screenshots, accessible mathematics, structural comparisons and a hashed report. Visual inspection of the captured pages remains a separate review step.

The workflow uses a fresh anonymous Chromium context and `contents: read`. It reads public, commit-pinned pages of this repository; it uses no account cookies or secrets and performs no repository writes. It runs on `furnish/**` branches and can be started manually after integration.

For an environment with Node.js, Python 3, Git, Playwright and MathJax installed, run the collector with this repository's full source SHA:

```bash
node verification/hosted_math/capture_hosted_math.cjs \
  --root . \
  --repository GoGoKo699/Quantum-Gibbs-Testing \
  --revision FULL_COMMIT_SHA \
  --output /tmp/gibbs-hosted-evidence
```

Use a new output directory for each run. The workflow uses Ubuntu 24.04 and installs Playwright 1.56.1 and MathJax 3.2.1 in a temporary dependency directory. Source compilation supplies the comparison reference; only captured GitHub content supplies the hosted evidence. Renderer diagnostics and structural equality do not establish scientific validity or replace visual review.
