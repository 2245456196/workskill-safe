---
name: proposal-flow-review-ready
description: >-
  Convert reviewed proposal notes into a decision package covering needs,
  stakeholders, solution scope, evidence gaps, objections, MVP selection,
  business assumptions, and slide-ready outputs.
---

# Proposal Flow to Review-Ready Package

## Purpose

Turn fragmented and reviewed proposal information into a structured package for decision-makers and reviewers.

## When to use

Use when a proposal has multiple stakeholders, incomplete evidence, mixed business and technical content, or feedback that requires structural revision.

## When not to use

Do not use on unreviewed source material. Do not invent evidence, adoption, prices, or results.

## Required inputs

- reviewed proposal notes
- intended decision-maker
- expected decision
- known constraints
- available evidence
- unresolved assumptions
- required output format

## Workflow

1. 確認提案目的、決策者與預期決策。
2. 將原始需求拆成問題、對象、場景與限制。
3. 分別整理各角色的痛點、採用誘因與反對理由。
4. 將方案拆成服務流程、技術模組、交付責任與資料邊界。
5. 選擇一個可在短週期驗證的最小可行版本。
6. 建立商業模式假設，但把未確認條件標記為待驗證。
7. 建立主張與證據對照表，不使用無來源的精確數字。
8. 模擬高層與審查角色的質疑，逐題調整內容架構。
9. 先完成高層決策摘要，再轉換為簡報頁面。
10. 依回饋區分必改、應補資料與可延後項目。
11. 完成資料、技術與交付邊界檢查。
12. 以第二個虛構案例測試流程是否可重複使用。

## Output contract

Follow `references/output-schema.md`. The output must include:

1. Executive decision summary
2. Stakeholder and pain-point matrix
3. Proposed service and technical scope
4. MVP choice and rationale
5. Business-model assumptions
6. Claim-to-evidence table
7. Reviewer objection and response table
8. Slide-page outline
9. Missing information and risks
10. Action list
11. Publication checklist

## Evidence rules

- Separate verified facts, assumptions, and missing data.
- Never create precise numbers without a source.
- Mark unsupported statements as `待驗證`.
- Keep evidence status visible in executive and slide-ready outputs.

## Privacy guardrails

- Use only reviewed source material.
- Remove organization, customer, person, project, date, value, URL, and path identifiers.
- Generalize unique combinations that could reveal the source context.
- Complete `docs/CONTEXTUAL_REIDENTIFICATION_CHECKLIST.md` before publication.
- Stop when authorization or publication status is uncertain.
- Require human review before public use.

## Validation checklist

- [ ] The expected decision is explicit.
- [ ] Stakeholder incentives and objections are separated.
- [ ] MVP scope is narrower than the full vision.
- [ ] Business assumptions are marked as assumptions.
- [ ] Every material claim has evidence status.
- [ ] Reviewer questions change the structure, not only wording.
- [ ] Each slide communicates one core judgment.
- [ ] The action list is present.
- [ ] Contextual re-identification review is complete.
- [ ] The workflow succeeds on a second synthetic case.
