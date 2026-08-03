# Database Cutover Recipe

Use this ordered, low-freedom workflow for destructive or production-adjacent database moves. Keep each step separately observable and stop on a failed gate.

## 1. Verify identities and destination state

- Resolve the exact source, destination, database, schema, container, and volume names from live inspection; do not rely on partial-name matches.
- Confirm the destination is empty or record the explicitly approved merge behavior.
- Verify source/destination version compatibility and required extensions, roles, ownership, and provider restrictions before taking the final backup.
- Define how writes will be quiesced or synchronized during the final backup and import. Do not treat an earlier dump as final while unaccounted writes can continue.
- Construct connection values without printing credentials. Keep secret retrieval separate from later commands and write only to an approved ignored file when persistence is necessary.

## 2. Create recoverable evidence

- Take a full source backup before importing or deleting anything.
- Record its absolute path, size, SHA-256, format, tool version, and a tested or clearly documented rollback command. State explicitly when restore has not been tested.
- Preserve the original backup unchanged. Perform any sanitation on a disposable copy.

## 3. Prepare and import

- Inspect the dump and importer help before selecting flags or subcommands.
- Check session settings such as `set_config('search_path', '', false)`. Prefer schema-qualified import and verification. If the destination tool requires normalization, remove or replace only the confirmed incompatible setting in the disposable import copy.
- Import into the verified destination. Capture the exit status without exposing the connection secret.

## 4. Verify deterministically

- Use schema-qualified identifiers such as `public.<table>` for all checks.
- Compare the expected schemas, tables, row counts, foreign keys, and owned sequences.
- Build digests from explicit columns and stable null/encoding rules. When text ordering affects the digest, order with deterministic collation such as `COLLATE "C"` on both databases.
- Investigate any mismatch before continuing; do not dismiss it as an environment difference without a deterministic recheck.

## 5. Exercise and clean up

- Run the smallest applicable local and production smoke tests after import.
- Observe the switched application long enough to detect delayed failures, using an explicitly approved window appropriate to the system.
- Delete the old database, container, volume, or credentials only after backup, deterministic verification, smoke tests, and the observation window all pass. Treat each target as a separate destructive action requiring explicit approval.
- Re-resolve every destructive target immediately before deletion and report what was removed, the remaining backup path and hash, and how to roll back.

## Required finish evidence

Report each item as `PASS`, `FAIL`, or `N/A` with a concrete reason:

- destination state and exact identities;
- write quiescence/synchronization and version/provider compatibility;
- backup, SHA-256, and rollback path;
- dump/session-setting handling;
- schema-qualified row, foreign-key, and sequence verification;
- deterministic digest and collation;
- smoke tests;
- observation window and cleanup approval;
- destructive cleanup status;
- secret exposure check.
