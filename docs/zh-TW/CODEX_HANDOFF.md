# Codex 接手說明

## 目前已完成

ChatGPT 已完成：

- 專案規格與隱私邊界
- 繁體中文維護文件
- Python CLI 初版
- 掃描、去識別化、Skill 生成與驗證
- 13 項本機測試
- lint、型別檢查、Demo 與打包驗證
- GitHub Issue／PR 模板與 CI 設定

因此 Codex 不需要重新建立整個專案。

## Codex 只處理

- GitHub Actions 的實際失敗
- 明確測試缺口
- 隱私規則的邊界案例
- 指定 Issue 的小範圍修正
- PR 程式審查與測試補強

## 不可自行執行

- 大幅改寫架構
- 加入外部服務、Telemetry 或雲端處理
- 使用真實公司或個人資料
- 發布 Release
- 提交 OpenAI 申請
