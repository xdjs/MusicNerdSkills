# Completion evals and finite closeout

Use when defining a substantive issue or closing a tracker with mixed implementation and acceptance evidence. Source: October 29, 2026 R&D, 39:05 and 47:05–49:05. This implements concrete evals now; autonomous merging remains a future discussion, not authorization.

## Before implementation

Map each original done-when to an observable check. Keep the scope proportional to the change; a UI bug may need one interaction, while research quality needs source-grounded cases.

| Requirement | Input / starting state | Expected result and failure condition | Evidence / environment | Bound |
| --- | --- | --- | --- | --- |
| User-observable behavior | Fixed fixture or exact interaction | What must happen; what would fail | Test, real flow, source revision, SHA | Cases, attempts, time or spend as relevant |

Freeze expected outcomes before execution. For model behavior, use grounded source passages, allow honest uncertainty only where the evidence is insufficient, and distinguish a useful correct answer from an unjustified refusal. Critical identity, privacy and fabricated-citation failures cannot be averaged away by a quality score. Keep diagnostic regressions separate from held-out examples. Do not prescribe a universal score or sample count; agree the bar for the actual requirement.

Use existing tests, fixtures and deployed evidence first. Record where mocks stop and real integrations begin. A new deployment method, database clone or fault campaign is not itself a product requirement; add it only when necessary to resolve a specific acceptance question. Shared writes, paid calls and configuration changes remain subject to the task's existing authorization and limits.

## Run and stop

Record exact code/environment/source revisions, inputs, actual outputs, citations, failures and unscored cases. A blocked run is not a pass. Keep earlier grades when the code, rubric or fixtures change and label any new run separately. State attempt/time/spend bounds before costly execution; report the cause of failure before retrying rather than rerunning until green.

## Closeout

Map the evidence back to the original requirements: passed, failed, unverified, or explicitly accepted/deferred by the owner. Separate shipped implementation, current behavior and accepted limitations. For old drafts, check whether the current implementation still contains the changed path before reviving them.

Every remaining item must be completed, moved to a linked focused follow-up, or explicitly deferred/declined by the user. Preserve the reason and dated attribution. Do not mark a failed eval passed because its limitation was accepted, or reopen accepted scope through new test-method requirements. Stop when the agreed criteria and owner dispositions are satisfied; keep normal PR and release gates.
