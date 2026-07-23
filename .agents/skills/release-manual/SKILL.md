---
name: release-manual
description: Release the FCS GitHub Pages manual from the current main HEAD by creating an immutable vYY.MM.PP patch tag, advancing the YY.MM series tag, deploying the Sphinx site, and verifying the live Japanese and English pages. Use when asked to tag, publish, deploy, or validate a new fcs-doc manual release; do not use for ordinary documentation edits or local previews.
---

# Release the FCS Manual

Follow this workflow in order. Treat `vYY.MM.PP` as an immutable release tag and
`YY.MM` as the moving tag consumed by `doc/versions.yaml` and the Pages builder.

## 1. Establish the release target

1. Take the requested patch tag as `release_tag`. Require the form
   `v[0-9]{2}.[0-9]{2}.[0-9]{2}`. If no version was supplied, infer it only when
   one unreleased version is unambiguous in `doc/01_updates/index.md`; otherwise
   ask for it.
2. Derive `series_tag` by removing the leading `v` and final dot component. For
   `v26.04.03`, use `26.04`.
3. Fetch only `main`, not all tags. This repository can contain unrelated local
   tags that conflict with the remote.
4. Record `release_sha=$(git rev-parse HEAD)` and require all of the following:
   - the current branch is `main`;
   - the worktree is clean;
   - `release_sha` equals `origin/main` after `git fetch --prune origin main`;
   - `doc/versions.yaml` lists `series_tag` first and its `tag` is `series_tag`;
   - `doc/01_updates/index.md` contains the patch version without the leading `v`;
   - neither the local nor remote `release_tag` already exists.

Stop and report discrepancies. Never guess a different commit or retag an
existing patch release.

## 2. Publish the immutable patch tag

Match the repository's existing lightweight-tag convention:

```bash
git tag "$release_tag" "$release_sha"
git push origin "refs/tags/$release_tag:refs/tags/$release_tag"
```

If the HTTPS remote cannot obtain credentials but `gh auth status` succeeds,
leave the configured remote unchanged and retry the exact ref through
`git@github.com:ZukunFCS/fcs-doc.git`.

Verify both values equal `release_sha`:

```bash
git rev-parse "$release_tag^{commit}"
git ls-remote --tags git@github.com:ZukunFCS/fcs-doc.git "refs/tags/$release_tag"
```

## 3. Advance the moving series tag

The patch-tag push does not deploy Pages. Dispatch the repository's built-in
workflow, which reads the first entry in `doc/versions.yaml` and force-advances
that series tag to `main` HEAD:

```bash
gh workflow run release_tag.yml --repo ZukunFCS/fcs-doc --ref main
```

Identify the newly created `Fast-forward release tag` run, save its run ID and
URL, then wait for it with `gh run watch RUN_ID --exit-status --interval 5`.
After success, require the remote `refs/tags/$series_tag` SHA to equal
`release_sha`. Do not manually force the immutable patch tag.

## 4. Build and deploy the manual

Dispatch the documentation workflow only after the series tag is verified:

```bash
gh workflow run documentations.yml --repo ZukunFCS/fcs-doc --ref main
```

Save the new documentation run ID and URL, then wait for it to complete
successfully. The workflow publishes `doc/_build/html` to `gh-pages`; GitHub
then starts a separate `pages build and deployment` run. Locate the Pages run
created after the documentation dispatch and wait for that run as well. Poll in
short intervals and keep the user updated at least once per minute.

If a run fails, inspect it with `gh run view RUN_ID --log-failed`. Fix or retry
only within the user's release scope. Do not delete or move a published patch
tag to conceal a failed deployment.

## 5. Verify GitHub and the live site

Verify all layers rather than relying on a green documentation job:

1. Fetch `gh-pages` and confirm its latest deploy commit corresponds to the
   documentation run.
2. Read `.build_manifest.json` from `origin/gh-pages` and require the
   `series_tag` entry's `tag_sha` to equal `release_sha`.
3. Require `gh api repos/ZukunFCS/fcs-doc/pages` to report `status: built` and
   the expected URL `https://zukunfcs.github.io/fcs-doc/`.
4. Fetch cache-busted live URLs until they show the release, allowing several
   minutes for CDN propagation:
   - `/$series_tag/jp/01_updates/index.html` contains the patch version;
   - `/$series_tag/en/01_updates/index.html` contains the patch version;
   - `/$series_tag/jp/index.html` and `/en/index.html` identify `series_tag`;
   - `/index.html` redirects or links to `series_tag`;
   - `/latest/jp/index.html` and `/latest/en/index.html` redirect to
     `series_tag`.
5. Confirm both `refs/tags/$release_tag` and `refs/tags/$series_tag` still equal
   `release_sha` on GitHub.

Use `curl -fsSL` and append `?verify=$release_sha` to bypass stale caches. Treat
missing text, HTTP failures, or a stale manifest as incomplete publication even
when Actions is green.

## 6. Report the release

Return the patch tag, series tag, exact release SHA, release-workflow URL,
documentation-workflow URL, Pages-workflow URL, and verified live Japanese and
English release-note URLs. Mention any warnings that do not block publication.
