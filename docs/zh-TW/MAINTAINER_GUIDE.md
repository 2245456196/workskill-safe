# 維護者操作指南

## 一般變更流程

```text
Issue
  ↓
功能分支
  ↓
實作與測試
  ↓
Pull Request
  ↓
隱私與程式審查
  ↓
合併
```

## 維護者每次需確認

- 變更是否仍符合 MVP 範圍
- 是否加入真實或可識別資料
- 是否增加網路傳輸或資料保存
- 是否弱化 fail-closed 行為
- 測試是否涵蓋正例、近似例與誤判風險
- README 是否與實際指令一致

## Codex 使用原則

Codex 不需要重新閱讀完整專案包，只需：

1. 閱讀 repo 的 `AGENTS.md` 與相關 Issue
2. 針對指定失敗或缺口修改
3. 執行測試
4. 開 PR
5. 不自行發布 Release 或提交 OpenAI 表單

## Pilot 原則

真實資料只在私人環境測試。GitHub 只留下：

- 聚合數字
- 完全虛構的重現案例
- 新增或調整的規則
- 對應 Issue、PR 與 Release
